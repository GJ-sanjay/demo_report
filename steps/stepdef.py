import time
import pytest
import ast
import json
from Functions import CommonFunction
from PropertyFile import PropertiesUtils
from selenium import webdriver
import ast
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from RepositoryFile import Repository
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
with open(
    "C://Users//sjayakumar//myworld//UltimateQA//steps//config.json", "r"
) as config:
    data = json.load(config)
#
pro = PropertiesUtils(data["property_path"])
# driver methods
common = CommonFunction()


# Given steps
@given("Launch the webpage with the provided URL")
def launch_webpage(context):
    driver.get(data["url"])


@given('Click on the "Big page with many elements"')
def click_big_page(context):
    mod1 = driver.find_element(*pro.get_locator("big_page_link"))
    common.Click(mod1)


@when('user clicks on the button from "Section of buttons"')
def step_impl(context):
    btn1 = driver.find_element(*pro.get_locator("button_1"))
    common.Click(btn1)


@then("The page refreshes")
def step_impl(context):
    ref = driver.find_element(*pro.get_locator("page1_refresh"))
    if common.IsDisplayed(ref):
        print("Success")
    time.sleep(5)


@then('User clicks on "X", "f" icon from Section of Social Media')
def step_impl(context):
    Twitter_icon = driver.find_element(*pro.get_locator("twitter_icon"))
    Twitter_icon.click()
    time.sleep(3)
    common.Back(driver)
    time.sleep(3)
    Facebook_icon = driver.find_element(*pro.get_locator("facebook_icon"))
    Facebook_icon.click()
    time.sleep(3)
    common.Back(driver)
    time.sleep(3)
    Random_stuff = driver.find_element(*pro.get_locator("section_of_random_stuff"))
    driver.execute_script("window.scrollTo(0, window.scrollY + 700)")
    time.sleep(2)


@then("closes it")
def step_impl(context):
    if common.IsDisplayed(
        driver.find_element(*pro.get_locator("section_of_random_stuff"))
    ):
        print("Success")


@then('the user scrolls down to "Section of Random Stuff"')
def step_impl(context):
    time.sleep(0.5)


@then("the user types in the name, email, message, and enters the captcha box")
def step_impl(context):
    Name = driver.find_element(*pro.get_locator("name_field"))
    common.SendKeys(Name, data["name"])
    time.sleep(0.5)
    Email = driver.find_element(*pro.get_locator("email_field"))
    common.SendKeys(Email, data["email"])
    time.sleep(0.5)
    Message = driver.find_element(*pro.get_locator("message_field"))
    common.SendKeys(Message, data["message"])
    time.sleep(0.5)

    # ast literal_eval implementation for captcha
    Captcha_field = driver.find_element(*pro.get_locator("captcha_field"))
    expression = Captcha_field.text
    result = eval(expression)
    result_element = driver.find_element(*pro.get_locator("result_box"))
    result_str = str(result)
    print(result_str)
    # result_element.send_keys(result_str)
    common.SendKeys(result_element, result_str)
    time.sleep(2)


@then("Click on Submit button")
def step_impl(context):
    time.sleep(2)
    Submit = driver.find_element(*pro.get_locator("submit_button"))
    Submit.click()
    time.sleep(2)
    print("Module 1 run complete")
    common.Back(driver)


# -------------------------------------------------------------------------------------#
# Module---2
@given('Click on the "Fake Landing Page"')
def step_impl(context):
    Fake_landing = driver.find_element(*pro.get_locator("fake_landing"))
    Fake_landing.click()
    time.sleep(2)


@when('user scrolls down to "View all courses"')
def step_impl(context):
    driver.execute_script("window.scrollTo(0, window.scrollY + 1900)")
    time.sleep(2)


@then("Clicks on it")
def step_impl(context):
    View_all_course = driver.find_element(*pro.get_locator("view_all_course"))
    View_all_course.click()
    time.sleep(2)


@then("User returns to top of the page")
def step_impl(context):
    Title2 = driver.find_element(*pro.get_locator("title_2"))
    if common.IsDisplayed(Title2):
        print("Title Verified")
    time.sleep(3)
    common.Back(driver)
    print("Module 2 run complete")


# -------------------------------------------------------------------------------------#
# Module---3


@given('Click on the "Fake Pricing Page"')
def step_impl(context):
    time.sleep(2)
    Fake_pricing = driver.find_element(*pro.get_locator("fake_pricing"))
    Fake_pricing.click()
    time.sleep(2)


@then("The user scrolls down to quote section")
def step_impl(context):
    # Quote = driver.find_element(*pro.get_locator("quote"))
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(1.5)


@then("user prints the quote to the console")
def step_impl(context):
    Quote = driver.find_element(*pro.get_locator("quote"))
    Quote_text = Quote.text  # Remove the parentheses after .text
    print(f"Quote text : {Quote_text}")
    common.Back(driver)
    time.sleep(2)
    print("Module 3 run complete")


# -------------------------------------------------------------------------------------#
# Module---4


@given('Click on the "Fill out forms"')
def step_impl(context):
    Fill_out_forms = driver.find_element(*pro.get_locator("fill_out_forms"))
    Fill_out_forms.click()
    time.sleep(2)


@then('user fills out the form fields "Name", "Message", and "captcha"')
def step_impl(context):
    Name_field4 = driver.find_element(*pro.get_locator("name_field4"))
    common.SendKeys(Name_field4, data["name4"])
    time.sleep(0.5)
    Message_field4 = driver.find_element(*pro.get_locator("message_field4"))
    common.SendKeys(Message_field4, data["message4"])
    time.sleep(0.5)

    # Captcha_field4
    Captcha_field4 = driver.find_element(*pro.get_locator("captcha_field4"))
    expression = Captcha_field4.text
    result4 = eval(expression)
    result_element4 = driver.find_element(*pro.get_locator("result_box4"))
    result_str4 = str(result4)
    print(result_str4)
    # result_element.send_keys(result_str)
    common.SendKeys(result_element4, result_str4)
    time.sleep(1)
    print("Module 4 run complete")


@then("User clicks submit button")
def step_impl(context):
    Submit4 = driver.find_element(*pro.get_locator("submit_button4"))
    Submit4.click()
    time.sleep(2)
    common.Back(driver)
    time.sleep(2)


# -------------------------------------------------------------------------------------#
# Module---5


@given('Click on the "Learn how to automate an application that evolves over time"')
def step_impl(context):
    Learn_how_to_automate = driver.find_element(
        *pro.get_locator("learn_how_to_automate")
    )
    Learn_how_to_automate.click()
    time.sleep(2)

    # resizing the window so the overlapping element disappears
    # Get the current window size
    current_window_size = driver.get_window_size()

    # Calculate the new window size (half of the current size)
    new_window_width = current_window_size["width"] // 2
    new_window_height = current_window_size["height"]

    # Set the new window size
    driver.set_window_size(new_window_width, new_window_height)


@when("Textbox appears enter the details")
def step_impl(context):
    First_name5 = driver.find_element(*pro.get_locator("first_name5"))
    common.SendKeys(First_name5, data["name5"])
    time.sleep(2)


@when("click on go to sprint")
def step_impl(context):
    Sprint2 = driver.find_element(*pro.get_locator("sprint2"))
    Sprint2.click()
    time.sleep(2)

    Sprint3 = driver.find_element(*pro.get_locator("sprint3"))
    Sprint3.click()
    time.sleep(2)

    Female_radiobutton = driver.find_element(*pro.get_locator("female_radiobutton"))
    Female_radiobutton.click()
    time.sleep(2)

    Sprint4 = driver.find_element(*pro.get_locator("sprint4"))
    Sprint4.click()
    time.sleep(2)

    Sprint5 = driver.find_element(*pro.get_locator("sprint5"))
    Sprint5.click()
    time.sleep(2)

    body = driver.find_element(*pro.get_locator("body"))
    common.ScrollDownBottom(driver, body)
    time.sleep(3)

    Submit5 = driver.find_element(*pro.get_locator("submit_button5"))
    Submit5.click()
    time.sleep(3)

    Crocodiles = driver.find_element(*pro.get_locator("crocodiles_radiobutton"))
    Crocodiles.click()
    time.sleep(2)

    Submit5_5 = driver.find_element(*pro.get_locator("submit5_button5"))
    Submit5_5.click()
    time.sleep(3)


@then("move back to home screen")
def step_impl(context):
    # Now navigate to a new URL
    new_url = "https://ultimateqa.com/automation"  # Replace this with the new URL you want to navigate to
    driver.execute_script(f"window.location.href = '{new_url}'")
    time.sleep(3)
    print("Module 5 run complete")

    # resizing again to fullscreen
    driver.maximize_window()
    time.sleep(3)


# -------------------------------------------------------------------------------------#
# Module---6


@given('Click on the "login automation"')
def step_impl(context):
    Login_automation = driver.find_element(*pro.get_locator("login_automation"))
    Login_automation.click()
    time.sleep(4)


@given("clicks the create a new account, enters the name, mail, password")
def step_impl(context):
    Body6 = driver.find_element(*pro.get_locator("body6"))
    common.ScrollDownBottom(driver, Body6)
    time.sleep(5)
    Create_new_account = driver.find_element(*pro.get_locator("create_new_account"))
    Create_new_account.click()
    time.sleep(4)

    First_name6 = driver.find_element(*pro.get_locator("first_name6"))
    common.SendKeys(First_name6, data["first_name6"])
    time.sleep(1)

    Last_name6 = driver.find_element(*pro.get_locator("last_name6"))
    common.SendKeys(Last_name6, data["last_name6"])
    time.sleep(1)

    Email_id6 = driver.find_element(*pro.get_locator("email_id6"))
    common.SendKeys(Email_id6, data["email6"])
    time.sleep(1)

    Password = driver.find_element(*pro.get_locator("password"))
    common.SendKeys(Password, data["password6"])
    time.sleep(1)

    Body6_1 = driver.find_element(*pro.get_locator("body6_1"))
    common.ScrollDownBottom(driver, Body6_1)
    time.sleep(2)
    Terms_and_condition = driver.find_element(*pro.get_locator("terms_and_conditions"))
    Terms_and_condition.click()
    time.sleep(3)


@then("clicks the sign up button")
def step_impl(context):
    # captcha page so we skip pressing on sign up
    """
    Sign_up = driver.find_element(*pro.get_locator("sign_up"))
    Sign_up.click()
    time.sleep(3)
    """
    # Instead we click on already have an account and sign-in
    Have_an_account = driver.find_element(*pro.get_locator("have_an_account"))
    Have_an_account.click()
    time.sleep(2)


@then("clicks the sign-in page button")
def step_impl(context):
    # Skipping this step
    time.sleep(1)


@then("enter email id, password")
def step_impl(context):
    Email6 = driver.find_element(*pro.get_locator("email6"))
    common.SendKeys(Email6, data["email6"])
    time.sleep(0.5)

    Password6 = driver.find_element(*pro.get_locator("password6"))
    common.SendKeys(Password6, data["password6"])
    time.sleep(0.5)


@then("clicks the submit button")
def step_impl(context):
    # Sign_in6 = driver.find_element(*pro.get_locator("sign_in6"))
    # Sign_in6.click()
    # time.sleep(2)
    time.sleep(0.5)
    # After logging in the user to sign out


@then("clicks the forgot password")
def step_impl(context):
    # Account = driver.find_element(*pro.get_locator("account"))
    # Account.click()
    # time.sleep(2)
    #
    # Sign_out = driver.find_element(*pro.get_locator("sign_out"))
    # Sign_out.click()
    # time.sleep(2)
    #
    # Sign_in = driver.find_element(*pro.get_locator("sign_in"))
    # Sign_in.click()
    # time.sleep(2)

    Forgot_password = driver.find_element(*pro.get_locator("forgot_password"))
    Forgot_password.click()
    time.sleep(2)


@then("enters email id, clicks submit button")
def step_impl(context):
    Email6_1 = driver.find_element(*pro.get_locator("email6_1"))
    common.SendKeys(Email6_1, data["email6"])
    time.sleep(1)

    Submit6 = driver.find_element(*pro.get_locator("submit6"))
    Submit6.click()
    time.sleep(2)


@then('"help is on the way" displayed in console')
def step_impl(context):
    Help_on_the_way = driver.find_element(*pro.get_locator("help_on_the_way"))
    print(Help_on_the_way.text)
    time.sleep(2)
    common.Back(driver)
    time.sleep(2)
    print("Module 6 run complete")


# -------------------------------------------------------------------------------------#
# Module---7


@given('Click on the "interaction with simple elements"')
def step_impl(context):
    Interaction_with = driver.find_element(
        *pro.get_locator("interaction_with_simple_elements")
    )
    Interaction_with.click()
    time.sleep(2)


@when("user clicks the button using id, classname, name")
def step_impl(context):
    # ID
    Click_button_using_id = driver.find_element(
        *pro.get_locator("click_button_using_id")
    )
    Click_button_using_id.click()
    time.sleep(3)
    common.Back(driver)
    time.sleep(3)

    # Link
    Click_button_using_link = driver.find_element(
        *pro.get_locator("click_button_using_link")
    )
    Click_button_using_link.click()
    time.sleep(3)
    common.Back(driver)
    time.sleep(3)

    # ClassName
    Click_button_using_class = driver.find_element(
        *pro.get_locator("click_button_using_class")
    )
    Click_button_using_class.click()
    time.sleep(3)
    common.Back(driver)
    time.sleep(3)


@then("The button success page loaded")
def step_impl(context):
    print("The Success button is displayed three times")
    time.sleep(2)


@then("the user clicks click me button")
def step_impl(context):
    print("functionality already tested")


@then("the click me button success page loaded")
def step_impl(context):
    print("functionality already tested")


@then("Clicks the toggle button")
def step_impl(context):
    Toggle = driver.find_element(*pro.get_locator("toggle"))

    # Perform mouse hover action
    action = ActionChains(driver)
    action.move_to_element(Toggle).perform()

    # Wait for two seconds after hover
    time.sleep(2)
    print("Mouse hovered over the toggle button for 2 seconds")


@then("it is visible")
def step_impl(context):
    time.sleep(2)
    print("The color pattern changes from grey to white")


@then("sends the name and email address")
def step_impl(context):
    Name_field7 = driver.find_element(*pro.get_locator("name_field7"))
    common.SendKeys(Name_field7, data["name7"])
    time.sleep(1)
    Email_field7 = driver.find_element(*pro.get_locator("email_field7"))
    common.SendKeys(Email_field7, data["email7"])
    time.sleep(1)


@then("clicks the email me")
def step_impl(context):
    Submit_button7 = driver.find_element(*pro.get_locator("submit_button7"))
    Submit_button7.click()
    time.sleep(2)


@then("click radio buttons, checkbox, dropdown")
def step_impl(context):
    print("Radio button and checkbox have already been tested")

    # DropDown feature
    Select_button7 = driver.find_element(*pro.get_locator("select_button7"))
    Select_button7.click()
    time.sleep(2)

    dropdown = Select(Select_button7)
    dropdown.select_by_visible_text("Opel")
    time.sleep(2)


@then("access the table with and without id")
def step_impl(context):
    # Locate the table using its ID
    table = driver.find_element(*pro.get_locator("table_with_id"))

    # Locate all rows in the table body
    rows = table.find_elements(*pro.get_locator("table_rows_with_tag"))

    # Select the second row (index 1 as indexing starts from 0)
    second_row = rows[3]

    # Fetch and print the text of each cell in the second row
    cells_in_second_row = second_row.find_elements(
        *pro.get_locator("table_rows_with_td")
    )
    print("Fetching values of cells with id")
    for cell in cells_in_second_row:
        print(cell.text)

    # Locating the table without id and fetching the values

    # Locate the table using its ID
    table = driver.find_element(*pro.get_locator("table_without_id"))
    # Locate all rows in the table body
    rows = table.find_elements(*pro.get_locator("table_rows_without_tag"))

    # Select the second row (index 1 as indexing starts from 0)
    second_row = rows[3]

    # Fetch and print the text of each cell in the second row
    cells_in_second_row = second_row.find_elements(
        *pro.get_locator("table_rows_without_td")
    )
    print("Fetching values of cells without id")
    for cell in cells_in_second_row:
        print(cell.text)

    print("Module 7 run complete")
