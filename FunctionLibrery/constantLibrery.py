
class ConstantLibrery:
    # Note:
    # Declare Web Object Locators here
    # Add 'LocatorType:' before the locator value eg : 'Xpath://input[@name="terms"]','Name:fld_username'
    # Web Object Name should be same in both 'getObjLocater' and 'getObjName' functions
    @staticmethod
    def getObjLocator(object):
        switcher = {
            # ******************* TheTestingWorld Application ************************
            # Signup Page
            'SignUp_page'       : 'Xpath://label[contains(text(),"Register")]',
            'SignUp_Login_Link': 'Xpath://label[contains(text(),"Login")]',
            'SignUp_UserName_TextBox': 'Name:fld_username',
            'SignUp_MailId_TextBox': 'Name:fld_email',
            'SignUp_Password_TextBox': 'Name:fld_password',
            'SignUp_CnfPassword_TextBox': 'Name:fld_cpassword',
            'SignUp_DateOfBirth_TextBox': 'Id:datepicker',
            'SignUp_PhoneNumber_TextBox': 'Name:phone',
            'SignUp_Address_TextBox': 'Name:address',
            'SignUp_Home_RadioBtn': 'Xpath://input[@name = "add_type" and @value ="home"]',
            'SignUp_Office_RadioBtn': 'Xpath://input[@name="add_type" and @value="office"]',
            'SignUp_Gender_DropDown': 'Name:sex',
            'SignUp_Country_DropDown': 'Name:country',
            'SignUp_State_DropDown': 'Name:state',
            'SignUp_City_DropDown': 'Name:city',
            'SignUp_ZipCode_TextBox': 'Name:zip',
            'SignUp_Terms_CheckBox': 'Xpath://input[@name="terms"]',
            'SignUp_SignUp_Btn': 'Xpath://input[@value="Sign up"]',

            # Login Page
            'Login_UserID_TextBox': 'Name:_txtUserName',
            'Login_Password_TextBox': 'Name:_txtPassword',
            'Login_Login_Btn': 'Xpath://input[@type="submit" and @value="Login"]',

            # Home Page
            'HomePage_Hover_Link' : 'Xpath://a[text()="Hover "]',
            'HomePage_ManageCustomer_Link' : 'Xpath:(//a[text()="Manage Customer "])[2]',
            'HomePage_Logout_Btn': 'Xpath://a[text()="logout"]',
            'HomePage_Sex_Dropdown': 'Xpath://select[@name="sex"]',
            'HomePage_PickList_ListBox_Isis': 'Xpath://*[@id="pickList"]/div/div[1]/select/option[text()="Isis"]',
            'HomePage_PickList_ListBox_Giovanna': 'Xpath://*[@id ="pickList"]/div/div[1]/select/option[text()="Giovanna"]',
            'HomePage_ViewLarge_ChooseFile' : 'Xpath://input[@id="file"]',
            'HomePage_ViewLarge_Upload':  'Xpath://input[@type="submit" and @value="Upload"]',
            'HomePage_TestingProdSite_Link' : 'Xpath://a[contains(text(),"thetestingworld.com")]',
            #WebTable
            'CherCherTech_Table_WebElement': 'Id:webtable',
            'CherCherTech_Link1_Link': 'Xpath://div[@id="toc"]/ul/li[1]/a',
            'CherCherTech_Link2_Link' : 'Xpath://div[@id="toc"]/ul/li[2]/a',
            'CherCherTech_JIRA_Link' : 'Xpath:(//a[@id="head"])[6]',
            'CherCherTech_JIRA_PageHeader' : 'Xpath://*[@id="toc"]/ul/li[1]/a',

            #Pages
            'CherCherTech_JIRA_Page': 'CherCherTech_JIRA_PageHeader',
            'SignUpPage'            :  'SignUp_page',
            'LoginPage'             :  'Login_UserID_TextBox',
            'HomePage'              :  'HomePage_Logout_Btn',

            # ******************* Mercury Application ************************
            # Sign Up page
            'MC_UserName_TextBox'   :  'Name:userName',
            'MC_Password_TextBox'   :  'Xpath://input[@name="password"]',
            'MC_SignIn_Button'      :  'Xpath://input[@name="login"]',
            'MC_SignOff_Link'       :  'Xpath://a[text() = "SIGN-OFF"]'
        }
        return switcher.get(object, False)

    # Note:
    # Declare Web Object Name here
    # Web Object Name should be same in both 'getObjLocator' and 'getObjName' functions
    @staticmethod
    def getObjDescription(object):

        switcher = {
            # Signup Page
            'SignUp_page'                : 'SignupPage',
            'SignUp_Login_Link'          : 'SignupPage - Login Link',
            'SignUp_UserName_TextBox'    : 'SignupPage - UserName TextBox',
            'SignUp_MailId_TextBox'      : 'SignupPage - MailId TextBox',
            'SignUp_Password_TextBox'    : 'SignupPage - Password TextBox',
            'SignUp_CnfPassword_TextBox' : 'SignupPage - Confirm Password TextBox',
            'SignUp_DateOfBirth_TextBox' : 'SignupPage - DateOfBirth TextBox',
            'SignUp_PhoneNumber_TextBox' : 'SignupPage - PhoneNumber TextBox',
            'SignUp_Address_TextBox'     : 'SignupPage - Address TextBox',
            'SignUp_Home_RadioBtn'       : 'SignupPage - AddressType Home RadioButton',
            'SignUp_Office_RadioBtn'     : 'SignupPage - AddressType Office RadioButton',
            'SignUp_Gender_DropDown'     : 'SignupPage - Gender DropDown',
            'SignUp_Country_DropDown'    : 'SignupPage - Country DropDown',
            'SignUp_State_DropDown'      : 'SignupPage - State DropDown',
            'SignUp_City_DropDown'       : 'SignupPage - City DropDown',
            'SignUp_ZipCode_TextBox'     : 'SignupPage - ZipCode TextBox',
            'SignUp_Terms_CheckBox'      : 'SignupPage - Terms and Conditions CheckBox',
            'SignUp_SignUp_Btn'          : 'SignupPage - SignUp Button',

            # Login Page
            'Login_UserID_TextBox'     : 'LoginPage - UserId Textbox',
            'Login_Password_TextBox'   : 'LoginPage - Password Textbox',
            'Login_Login_Btn'          : 'LoginPage - Login Button',

            #Home Page
            'HomePage_Hover_Link'                :  'HomePage - Hover Link',
            'HomePage_ManageCustomer_Link'       :  'HomePage - ManageCustomer Link',
            'HomePage_Logout_Btn'                : 'HomePage - Logout Button',
            'HomePage_Sex_Dropdown'              : 'HomePage - Sex Dropdown under \'MyProfile\' section',
            'HomePage_PickList_ListBox_Isis'     : 'HomePage - From PickList "Isis" under \'JQuery Dual List Box Demo\' section',
            'HomePage_PickList_ListBox_Giovanna' : 'HomePage - From PickList "Giovanna" under \'JQuery Dual List Box Demo\' section',
            'HomePage_ViewLarge_ChooseFile'      : 'HomePage - View Large Section "Choose File" button',
            'HomePage_ViewLarge_Upload'          : 'HomePage - View Large Section "Upload" button',
            'HomePage_TestingProdSite_Link'      :  'HomePage - Thetestingworld.com Link',
            # WebTable
            'CherCherTech_Table_WebElement': 'CherCherTech - WebTable',
            'CherCherTech_Link1_Link': 'CherCherTech - Web Table in Selenium Python Bindings Link',
            'CherCherTech_Link2_Link': 'CherCherTech - Custom WebTable in Selenium Python bindings Link',
            'CherCherTech_JIRA_Link': 'CherCherTech - JIRA Link',

            'CherCherTech_JIRA_PageHeader': 'CherCherTech - JIRA - Page header',

            # Pages
            'CherCherTech_JIRA_Page' : 'CherCherTech - JIRA - Page',
            'SignUpPage'             : 'Testing World Signup page',
            'LoginPage'              : 'Testing World Login Page',
            'HomePage'               : 'Testing World Home Page',

            # ******************* Mercury Application ************************
            # Sign Up page
            'MC_UserName_TextBox': 'Login Page - UserName TextBox',
            'MC_Password_TextBox': 'Login Page - Password TextBox',
            'MC_SignIn_Button'   : 'Login Page - SignIn Button',
            'MC_SignOff_Link'    : 'Home Page - SignOff Link'
        }
        return switcher.get(object,'ObjectDescriptionNotDefined(in constantLibrary)')
    # ------------------------------------------------------------------------------------------------------------------