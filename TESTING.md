# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
Direct links to the results have been added unless made impossible due to login/authentication restrictions.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| library | [add_book.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/templates/library/add_book.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Flibrary%2Fadd%2F) | ![screenshot](documentation/testing/validation/html-library-add_book.png) | No errors or warnings |
| library | [edit_book.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/templates/library/edit_book.html) | n/a | ![screenshot](documentation/testing/validation/html-library-edit_book.png) | No errors or warnings |
| library | [library.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/templates/library/library.html) | n/a | ![screenshot](documentation/testing/validation/html-library.png) | No errors or warnings |
| library | [sales.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/templates/library/sales.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Flibrary%2Fsales%2F) | ![screenshot](documentation/testing/validation/html-library-sales.png) | No errors or warnings |
| pages | [about.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/templates/pages/about.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing/validation/html-pages-about.png) | No errors or warnings |
| pages | [home.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/templates/pages/home.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2F) | ![screenshot](documentation/testing/validation/html-pages-home.png) | No errors or warnings |
| templates | [login.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/account/login.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/validation/html-templates-login.png) | There is one html validation error related to an aria-describedby attribute but this caused by the usage of Django AllAuth and Crispy Forms packages and is outside of my control.  |
| templates | [logout.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/account/logout.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Faccounts%2Flogout%2F) | ![screenshot](documentation/testing/validation/html-templates-logout.png) | No errors or warnings |
| templates | [signup.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/account/signup.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/validation/html-templates-signup.png) | No errors or warnings |
| templates | [password_reset.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/account/signup.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F) | ![screenshot](documentation/testing/validation/html-templates-password-reset.png) | No errors or warnings |
| templates | [password_reset_done.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/account/signup.html) | [Results Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Faccounts%2Fpassword%2Freset%2Fdone%2F) | ![screenshot](documentation/testing/validation/html-templates-password-reset-done.png) | No errors or warnings |
| templates | [404.html](https://github.com/Gary-Burke/book-lovers-market/blob/main/templates/404.html) | n/a | ![screenshot](documentation/testing/validation/html-templates-404.png) | No errors or warnings |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/Gary-Burke/book-lovers-market/blob/main/static/css/style.css) | [Results Link](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbook-lovers-market-4a712f119c48.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings) | ![screenshot](documentation/testing/validation/css-static-style.png) | All warnings were checked and can be safely ignored, as they are related to CSS variables and vendor extensions from Autoprefixer CSS online. |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | [add.js](https://github.com/Gary-Burke/book-lovers-market/blob/main/static/js/add.js) | ![screenshot](documentation/testing/validation/js-static-add.png) | No warnings or errors |
| static | [library.js](https://github.com/Gary-Burke/book-lovers-market/blob/main/static/js/library.js) | ![screenshot](documentation/testing/validation/js-static-library.png) | Warning can be ignored as it is related to the external Bootstrap library |
| static | [sales.js](https://github.com/Gary-Burke/book-lovers-market/blob/main/static/js/sales.js) | ![screenshot](documentation/testing/validation/js-static-sales.png) | Warning can be ignored as it is related to the external Bootstrap library |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bookloversmarket | [settings.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/bookloversmarket/settings.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/bookloversmarket/settings.py) | ![screenshot](documentation/testing/validation/py-bookloversmarket-settings.png) | No errors found |
| bookloversmarket | [urls.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/bookloversmarket/urls.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/bookloversmarket/urls.py) | ![screenshot](documentation/testing/validation/py-bookloversmarket-urls.png) | No errors found |
| library | [admin.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/admin.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/admin.py) | ![screenshot](documentation/testing/validation/py-library-admin.png) | No errors found |
| library | [forms.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/forms.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/forms.py) | ![screenshot](documentation/testing/validation/py-library-forms.png) | No errors found |
| library | [models.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/models.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/models.py) | ![screenshot](documentation/testing/validation/py-library-models.png) | No errors found |
| library | [test_forms.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/test_forms.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/test_forms.py) | ![screenshot](documentation/testing/validation/py-library-test_forms.png) | No errors found |
| library | [urls.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/urls.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/urls.py) | ![screenshot](documentation/testing/validation/py-library-urls.png) | No errors found |
| library | [views.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/library/views.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/library/views.py) | ![screenshot](documentation/testing/validation/py-library-views.png) | No errors found |
| root | [manage.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/manage.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/manage.py) | ![screenshot](documentation/testing/validation/py-manage.png) | No errors found |
| pages | [admin.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/admin.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/admin.py) | ![screenshot](documentation/testing/validation/py-pages-admin.png) | No errors found |
| pages | [forms.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/forms.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/forms.py) | ![screenshot](documentation/testing/validation/py-pages-forms.png) | No errors found |
| pages | [models.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/models.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/models.py) | ![screenshot](documentation/testing/validation/py-pages-models.png) | No errors found |
| pages | [test_forms.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/test_forms.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/test_forms.py) | ![screenshot](documentation/testing/validation/py-pages-test_forms.png) | No errors found |
| pages | [urls.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/urls.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/urls.py) | ![screenshot](documentation/testing/validation/py-pages-urls.png) | No errors found |
| pages | [views.py](https://github.com/Gary-Burke/book-lovers-market/blob/main/pages/views.py) | [Results Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/book-lovers-market/main/pages/views.py) | ![screenshot](documentation/testing/validation/py-pages-views.png) | No errors found |

## Responsiveness

I've tested my deployed project to check for responsive design.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/responsiveness/mobile-home.png) | ![screenshot](documentation/testing/responsiveness/tablet-home.png) | ![screenshot](documentation/testing/responsiveness/desktop-home.png) | Works as expected |
| About | ![screenshot](documentation/testing/responsiveness/mobile-about.png) | ![screenshot](documentation/testing/responsiveness/tablet-about.png) | ![screenshot](documentation/testing/responsiveness/desktop-about.png) | Works as expected |
| Library | ![screenshot](documentation/testing/responsiveness/mobile-library.png) | ![screenshot](documentation/testing/responsiveness/tablet-library.png) | ![screenshot](documentation/testing/responsiveness/desktop-library.png) | Works as expected |
| Add Book | ![screenshot](documentation/testing/responsiveness/mobile-add-book.png) | ![screenshot](documentation/testing/responsiveness/tablet-add-book.png) | ![screenshot](documentation/testing/responsiveness/desktop-add-book.png) | Works as expected |
| Add Book Manual | ![screenshot](documentation/testing/responsiveness/mobile-add-book-manual.png) | ![screenshot](documentation/testing/responsiveness/tablet-add-book-manual.png) | ![screenshot](documentation/testing/responsiveness/desktop-add-book-manual.png) | Works as expected |
| Edit Book | ![screenshot](documentation/testing/responsiveness/mobile-edit-book.png) | ![screenshot](documentation/testing/responsiveness/tablet-edit-book.png) | ![screenshot](documentation/testing/responsiveness/desktop-edit-book.png) | Works as expected |
| Sales | ![screenshot](documentation/testing/responsiveness/mobile-sales.png) | ![screenshot](documentation/testing/responsiveness/tablet-sales.png) | ![screenshot](documentation/testing/responsiveness/desktop-sales.png) | Works as expected |
| Register | ![screenshot](documentation/testing/responsiveness/mobile-register.png) | ![screenshot](documentation/testing/responsiveness/tablet-register.png) | ![screenshot](documentation/testing/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/testing/responsiveness/mobile-login.png) | ![screenshot](documentation/testing/responsiveness/tablet-login.png) | ![screenshot](documentation/testing/responsiveness/desktop-login.png) | Works as expected |
| Password Reset | ![screenshot](documentation/testing/responsiveness/mobile-password-reset.png) | ![screenshot](documentation/testing/responsiveness/tablet-password-reset.png) | ![screenshot](documentation/testing/responsiveness/desktop-password-reset.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Edge | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/browsers/chrome-home.png) | ![screenshot](documentation/testing/browsers/firefox-home.png) | ![screenshot](documentation/testing/browsers/edge-home.jpeg) | Works as expected |
| About | ![screenshot](documentation/testing/browsers/chrome-about.png) | ![screenshot](documentation/testing/browsers/firefox-about.png) | ![screenshot](documentation/testing/browsers/edge-about.jpeg) | Works as expected |
| Register | ![screenshot](documentation/testing/browsers/chrome-register.png) | ![screenshot](documentation/testing/browsers/firefox-register.png) | ![screenshot](documentation/testing/browsers/edge-register.jpeg) | Works as expected |
| Login | ![screenshot](documentation/testing/browsers/chrome-login.png) | ![screenshot](documentation/testing/browsers/firefox-login.png) | ![screenshot](documentation/testing/browsers/edge-login.jpeg) | Works as expected |
| Sales | ![screenshot](documentation/testing/browsers/chrome-sales.png) | ![screenshot](documentation/testing/browsers/firefox-sales.png) | ![screenshot](documentation/testing/browsers/edge-sales.jpeg) | Works as expected |
| Library | ![screenshot](documentation/testing/browsers/chrome-library.png) | ![screenshot](documentation/testing/browsers/firefox-library.png) | ![screenshot](documentation/testing/browsers/edge-library.jpeg) | Works as expected |
| Add Book | ![screenshot](documentation/testing/browsers/chrome-add-book.png) | ![screenshot](documentation/testing/browsers/firefox-add-book.png) | ![screenshot](documentation/testing/browsers/edge-add-book.jpeg) | Works as expected |
| Add Book Manual | ![screenshot](documentation/testing/browsers/chrome-add-book-manual.png) | ![screenshot](documentation/testing/browsers/firefox-add-book-manual.png) | ![screenshot](documentation/testing/browsers/edge-add-book-manual.jpeg) | Works as expected |
| Edit Book | ![screenshot](documentation/testing/browsers/chrome-edit-book.png) | ![screenshot](documentation/testing/browsers/firefox-edit-book.png) | ![screenshot](documentation/testing/browsers/edge-edit-book.jpeg) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/testing/lighthouse/mobile-register.png) | ![screenshot](documentation/testing/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/testing/lighthouse/mobile-login.png) | ![screenshot](documentation/testing/lighthouse/desktop-login.png) |
| Home | ![screenshot](documentation/testing/lighthouse/mobile-home.png) | ![screenshot](documentation/testing/lighthouse/desktop-home.png) |
| About | ![screenshot](documentation/testing/lighthouse/mobile-about.png) | ![screenshot](documentation/testing/lighthouse/desktop-about.png) |
| Library | ![screenshot](documentation/testing/lighthouse/mobile-library.png) | ![screenshot](documentation/testing/lighthouse/desktop-library.png) |
| Add Book | ![screenshot](documentation/testing/lighthouse/mobile-add-book.png) | ![screenshot](documentation/testing/lighthouse/desktop-add-book.png) |
| Add Book Manual | ![screenshot](documentation/testing/lighthouse/mobile-add-book-manual.png) | ![screenshot](documentation/testing/lighthouse/desktop-add-book-manual.png) |
| Edit Book | ![screenshot](documentation/testing/lighthouse/mobile-edit-book.png) | ![screenshot](documentation/testing/lighthouse/desktop-edit-book.png) |
| Sales | ![screenshot](documentation/testing/lighthouse/mobile-sales.png) | ![screenshot](documentation/testing/lighthouse/desktop-sales.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I would like to see my logged in status clearly displayed | so that my user experience on the site can be smooth. | ![screenshot](documentation/features/status.png) |
| As the owner | I would like it to be mandatory for users to use a username and e-mail for sign up | so that these details are never missing from sales listings. | ![screenshot](documentation/features/signup-credentials.png) |
| As a user | I would like to be able to request to reset my password if I forget it| so that I can still access my account. | ![screenshot](documentation/features/forgot-password.png) |
| As a user | I would like to see a clean and clear home page | so that I can know what to expect from this website. | ![screenshot](documentation/features/home.png) |
| As a user | I would like to have a consistent navigation bar at the top | so that I can easily navigate to the pages I want to visit. | ![screenshot](documentation/features/navbar.png) |
| As a user | I would like to see social media links in the footer | so that I can get in touch and stay up to date with the business and its products. | ![screenshot](documentation/features/footer.png) |
| As a user | I would like to see an about page | so that I can read about the busniess concept in more detail and provide feedback. | ![screenshot](documentation/features/about.png) |
| As a user | I would like to be able to add the books that I own to my library with an ISBN | so that I can have a digital overview of all my books. | ![screenshot](documentation/features/library-isbn.png) |
| As a user | I would like to be able to add the books that I own to my library manually | so that I can still have them even when the ISBN is not found. | ![screenshot](documentation/features/library-manual.png) |
| As a user | I would like to view my library | so that I can view all of my books. | ![screenshot](documentation/features/library.png) |
| As a user | I would like to filter my books | so that I can see books based on their status. | ![screenshot](documentation/features/library-filter.png) |
| As a user | I would like to edit the books in my library | so that I can maintain my library according to my preferences. | ![screenshot](documentation/features/library-edit.png) |
| As a user | I would like to delete the books in my library | so that I can maintain my library according to my preferences. | ![screenshot](documentation/features/library-delete.png) |
| As a user | I would like to be able to choose how my books are sorted | so that I can arrange them according to my preferences. | ![screenshot](documentation/features/library-sort.png) |
| As a user | I would like to view all books listed for sale | so that I can contact the owner to buy them. | ![screenshot](documentation/features/sales.png) |
| As the owner | I would like to be able to read the feedback submitted by users | so that I can adapt and improve my business as needed. | ![screenshot](documentation/features/admin-feedback.png) |
| As the owner | I would like to be able to edit and update the content on the Home Page | so that I can display a new book/reading quote every month. | ![screenshot](documentation/features/admin-home.png) |
| As a user | I would like to filter the books on the sales page based on search criteria | so that I can find books based on what I need. | ![screenshot](documentation/features/sales-search.png) |
| As a user | I would like to filter the books in my library based on search criteria | so that I can find my books based on what I need. | ![screenshot](documentation/features/library-search.png) |
| As a user | I would like to be able to click on a book for sale and see further details | so that I can find the contact information and additional information on the book. | ![screenshot](documentation/features/book-detail.png) |

## Defensive Programming

### Manual Testing

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Library | Only a logged in user should have access | As a logged out user I clicked on the Library nav link | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/library-nav.png) |
| Library | Only a logged in user should have access | As a logged out user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/library-url.png) |
| Library Add Book | Only a logged in user should be able to add a book to their library | As a logged out user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/add-book-url.png) |
| Library Add Book Manually | Only a logged in user should be able to add a book to their library | As a logged out user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/add-book-manual-url.png) |
| Library Edit Book | Only a logged in user should be able to edit a book in their library | As a logged out user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/add-book-url.png) |
| Library Delete Book | Only a logged in user should be able to delete a book from their library | As a logged out user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/delete-book-url.png) |
| Library Edit Book | A logged in user should not be able to edit a book from another user's library | As a logged in user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/edit-book-url-user.png) |
| Library Delete Book | A logged in user should not be able to delete a book from another user's library | As a logged in user I typed in the url for the page directly | The app informs and prevents access as expected | ![screenshot](documentation//testing/defensive/delete-book-url-user.png) |
| 404 | When a broken url is typed in the personalized 404 message should appear | I typed in a non-existent url | The app informs the user and they can safely navigate home | ![screenshot](documentation//testing/defensive/404.png) |

### Automated Testing

I have conducted a series of automated tests on my application to test all of my forms.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

Below are the results of these tests:

| App | Criteria | Screenshot | Notes |
| --- | --- | --- | --- |
| pages | Feedback Form was tested to ensure all fields are valid and no field is empty | ![screenshot](documentation/testing/defensive/tests-pages-result.png) | All defensive programming and testing was successfull |
| library | ISBN Form was tested to ensure all fields are valid and no field is empty | ![screenshot](documentation/testing/defensive/tests-library-result.png) | All defensive programming and testing was successfull |
| library | Edit Book Form was tested to ensure all fields are valid and no field is empty | ![screenshot](documentation/testing/defensive/tests-library-result.png) | All defensive programming and testing was successfull |
| library | Add Book Manually Form was tested to ensure all fields are valid and no field is empty | ![screenshot](documentation/testing/defensive/tests-library-result.png) | All defensive programming and testing was successfull |

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Gary-Burke/book-lovers-market?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Gary-Burke/book-lovers-market/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Gary-Burke/book-lovers-market/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Gary-Burke/book-lovers-market/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/gh/bugs-closed.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Gary-Burke/book-lovers-market?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/Gary-Burke/book-lovers-market/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/Gary-Burke/book-lovers-market/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/gh/bugs-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `320px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | n/a |
| There is one html validation error related to an aria-describedby attribute but this caused by the usage of Django AllAuth and Crispy Forms packages and is outside of my control. | ![screenshot](documentation/testing/validation/html-templates-login.png) |


> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

