"""IN subscriber profile handling module
"""
from datetime import datetime

from intelecom.intelecom import INConnection

from app.models.user import User


class INRequestHandler():
    """Handles requests to the IN.
    """

    def __init__(self, host: str, port: int, buffer_size: int):
        """Constructor

        Parameters
        ----------
        host : str
            IN server IP.
        port : int
            IN socket port.
        buffer_size : int
            IN command buffer size.
        """
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

    def account_info(self, msisdn: str, current_user: User) -> dict:
        """Get the MSISDN account information.

        Parameters
        ----------
        msisdn : str
            MSISDN number for the account whose account information is being
            required.

        current_user : User
            User performing the profile status query.

        Returns
        -------
        dict
            Transaction details and the account information.
        """
        with INConnection(
                self.host,
                current_user.mml_username,
                current_user.mml_password,
                self.port,
                self.buffer_size) as in_connection:

            query_result = in_connection.display_account_info(msisdn)
            balance = float(query_result['ACCLEFT'])
            subscriber_type = query_result['SUBSCRIBERTYPE']
            account_status = int(query_result['ACNTSTAT'])

            profile_info = {
                'mobileNumber': msisdn,
                'balance': balance,
                'subscriberProfile': subscriber_type
            }

            temporary_suspend_date = datetime.strptime(
                query_result['CALLSERVSTOP'],
                '%Y-%m-%d'
            )
            temporarily_suspended = (temporary_suspend_date < datetime.today())
            if account_status == 1 and not temporarily_suspended:
                profile_info['status'] = 'ACTIVE'
            else:
                profile_info['status'] = 'NOT ACTIVE'

            return profile_info

    def debit_airtime(self, msisdn: str, amount: float, current_user: User,):
        """Debits the MSISDN account with the new amount..

        Parameters
        ----------
        msisdn : str
            MSISDN number for the account whose balance to be debited.
        amount : float
            Money to be debited on a MSISDN account.
        current_user : User
            User performing the deduction amount query.

        Returns
        -------
        bool
            Returns True if the MSISDN account balance is debited, False otherwise.
        """
        with INConnection(
                self.host,
                current_user.mml_username,
                current_user.mml_password,
                self.port,
                self.buffer_size) as in_connection:

            return in_connection.debit_account(
                msisdn,
                amount,
                current_user.mml_username
            )

    def credit_airtime(self, msisdn: str, amount: float, current_user: User):
        """Credits the MSISDN account with a new amount.

        Parameters
        ----------
        msisdn : str
            MSISDN number for the account whose balance is to be credited.
        amount : float
            Money to be credited on a MSISDN account.
        current_user : User
            User performing the crediting account query.

        Returns
        -------
        bool
            Returns True if the MSISDN account balance is credited False otherwise.
        """
        with INConnection(
                self.host,
                current_user.mml_username,
                current_user.mml_password,
                self.port,
                self.buffer_size) as in_connection:

            return in_connection.credit_account(
                msisdn,
                amount,
                current_user.mml_username
            )

    def purchase_package(
            self,
            msisdn: str,
            current_profile: str,
            current_user: User,
            package_type: str,
            package_grade: str = None) -> dict:
        """[summary]

        Parameters
        ----------
        msisdn : str
            Mobile number purhasing the package.

        current_profile : str
            Current profile of the MSISDN.

        package_type : str
            Package type being purchased.

        package_grade : str
            Package grade of the package type being purchased.

        Returns
        -------
        dict
            Details of MSISDN, packageType, packageGrade, ProfileBefore,
            profileAfter returned.
        """
        with INConnection(
                self.host,
                current_user.mml_username,
                current_user.mml_password,
                self.port,
                self.buffer_size) as in_connection:

            package_purchased = in_connection.purchase_package(
                msisdn,
                package_type,
                package_grade
            )

            if package_purchased:
                operation_result = 'OK'
            else:
                operation_result = 'FAILED'

            return {
                'operationResult': operation_result,
                'msisdn': msisdn,
                'packageType': package_type,
                'packageGrade': package_grade
            }
