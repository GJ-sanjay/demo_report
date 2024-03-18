class Repository:
    mod1 = (
        {
            "big_page_link": "Big page with many elements",
            "button_1": "(//a[@class='et_pb_button et_pb_button_0 et_pb_bg_layout_light'])[1]",
            "page1_refresh": "Skills_Improved",
            "twitter_icon": "(//a[@title='Follow on Twitter'])[1]",
            "facebook_icon": "(//a[contains(@title,'Follow on Facebook')])[1]",
            "section_of_random_stuff": "//span[@id='Section_of_Random_Stuff']",
            "name_field": "//input[@id='et_pb_contact_name_0']",
            "email_field": "//input[@id='et_pb_contact_email_0']",
            "message_field": "(//textarea[@id='et_pb_contact_message_0'])[1]",
            "captcha_field": "//span[@class='et_pb_contact_captcha_question']",
            "submit_button": "(//button[@name='et_builder_submit_button'][normalize-space()='Submit'])[1]",
            "result_box": "(//input[@name='et_pb_contact_captcha_0'])[1]",
        },
    )
    mod2 = (
        {
            "fake_landing": "//a[normalize-space()='Fake Landing Page']",
            "view_all_course": "(//a[@class='et_pb_button et_pb_button_2 et_animated et_hover_enabled et_pb_bg_layout_light'])[1]",
            "title2": "(//h1[normalize-space()='Learn to Code Websites, Apps & Games'])[1]",
        },
    )
    mod3 = (
        {
            "fake_pricing": "Fake Pricing Page",
            "quote": "//span[contains(text(),'Cras malesuada fermentum sollicitudin. Ut at nunc ut lectus interdum consectetur et quis erat. Etiam vel lacus ex.')]",
        },
    )
    mod4 = {
        "fill_out_forms": "Fill out forms",
        "name_field4": "(//input[@id='et_pb_contact_name_1'])[1]",
        "message_field4": "(//textarea[@id='et_pb_contact_message_1'])[1]",
        "captcha_field4": "(//span[@class='et_pb_contact_captcha_question'])[1]",
        "result_box4": "(//input[@name='et_pb_contact_captcha_1'])[1]",
        "submit_button4": "(//button[@name='et_builder_submit_button'][normalize-space()='Submit'])[2]",
    }
    mod5 = (
        {
            "learn_how_to_automate": "Learn how to automate an application",
            "first_name5": "firstname",
            "sprint2": "(//a[normalize-space()='Go to the next sprint'])[1]",
            "sprint3": "(//a[normalize-space()='Go to sprint 3'])[1]",
            "female_radiobutton": "//input[@value='female']",
            "sprint4": "//a[normalize-space()='Go to sprint 4']",
            "sprint5": "//a[text()='Go to sprint 5']",
            "submit_button5": "//input[@type='submit']",
            "crocodiles_radiobutton": "//input[@value='crocodiles']",
            "submit5_button5": "//input[@type='submit']",
            "body": "/html/body",
        },
    )
    mod6 = (
        {
            "login_automation": "//a[normalize-space()='Login automation']",
            "body6": "/html/body",
            "create_new_account": "//a[normalize-space()='Create a new account']",
            "first_name6": "(//input[@id='user[first_name]'])[1]",
            "last_name6": "(//input[@id='user[last_name]'])[1]",
            "email_id6": "(//input[@id='user[email]'])[1]",
            "password": "user[password]",
            "body6_1": "/html/body",
            "terms_and_conditions": "(//input[@id='user[terms]'])[1]",
            "sign_up": "(//button[normalize-space()='Sign up'])[1]",
            "account": "(//i[@class='fa fa-caret-down'])[1]",
            "sign_out": "(//a[normalize-space()='Sign Out'])[1] ",
            "sign_in": "//a[normalize-space()='Sign In']",
            "email6": "(//input[@id='user[email]'])[1]",
            "password6": "(//input[@id='user[password]'])[1]",
            "sign_in6": "(//button[normalize-space()='Sign in'])[1]",
            "forgot_password": "(//a[normalize-space()='Forgot Password?'])[1]",
            "email6_1": "(//input[@id='user[email]'])[1]",
            "submit6": "(//input[@name='commit'])[1]",
            "help_on_the_way": "(//h2[normalize-space()='Help is on the way!'])[1]",
            "have_an_account": "(//a[normalize-space()='I already have an account!'])[1]",
        },
    )
    mod7 = {
        "interaction_with_simple_elements": "Interactions with simple elements",
        "click_button_using_id": "//a[@id='idExample']",
        "click_button_using_link": "Click me using this link text!",
        "click_button_using_class": "//button[@class='buttonClass']",
        "toggle": "//h5[text()='Open toggle to read text']",
        "name_field7": "et_pb_contact_name_0",
        "email_field7": "et_pb_contact_email_0",
        "submit_button7": "et_builder_submit_button",
        "select_button7": "//div[@class='et_pb_blurb_description']//select",
        "table_with_id": "//table[@id='htmlTableId']",
        "table_rows_with_tag": "//table[@id='htmlTableId']//tr",
        "table_rows_with_td": "//table[@id='htmlTableId']//tr//td",
        "table_without_id": "//h2[text()='HTML Table with no id']/following-sibling::table",
        "table_rows_without_tag": "//h2[text()='HTML Table with no id']/following-sibling::table//tr",
        "table_rows_without_td": "//h2[text()='HTML Table with no id']/following-sibling::table//tr//td",
    }
