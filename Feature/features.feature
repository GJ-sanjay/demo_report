Feature: Launch the Ultimate QA website & automate it.

Background:
  Given Launch the webpage with the provided URL

@mod1
Scenario: Automating the "Big page with many elements" page
  Given Click on the "Big page with many elements"
  When user clicks on the button from "Section of buttons"
  Then The page refreshes
  And User clicks on "X", "f" icon from Section of Social Media
  Then closes it
  And the user scrolls down to "Section of Random Stuff"
  And the user types in the name, email, message, and enters the captcha box
  And Click on Submit button

@mod2
Scenario: Automating the "Fake Landing Page" page.
  Given Click on the "Fake Landing Page"
  When user scrolls down to "View all courses"
  Then Clicks on it
  And User returns to top of the page

@mod3
Scenario: Automating the "Fake Pricing" page
  Given Click on the "Fake Pricing Page"
  Then The user scrolls down to quote section
  And user prints the quote to the console

@mod4
Scenario: Automating the "Fill out forms" page
  Given Click on the "Fill out forms"
  Then user fills out the form fields "Name", "Message", and "captcha"
  And User clicks submit button

@mod5
Scenario: Automating the "Learn how to automate an application that evolves over time" page
  Given Click on the "Learn how to automate an application that evolves over time"
  When Textbox appears enter the details
  And click on go to sprint
  Then move back to home screen

@mod6
Scenario: Automating the "Big page with many elements" page
  Given Click on the "login automation"
  And clicks the create a new account, enters the name, mail, password
  Then clicks the sign up button
  And clicks the sign-in page button
  And enter email id, password
  Then clicks the submit button
  And clicks the forgot password
  And enters email id, clicks submit button
  Then "help is on the way" displayed in console

@mod7
Scenario: Automating the "interaction with simple elements " page
  Given Click on the "interaction with simple elements"
  When user clicks the button using id, classname, name
  Then The button success page loaded
  And the user clicks click me button
  Then the click me button success page loaded
  And Clicks the toggle button
  Then it is visible
  And sends the name and email address
  Then clicks the email me
  And click radio buttons, checkbox, dropdown
  And access the table with and without id
