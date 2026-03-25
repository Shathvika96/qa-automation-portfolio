# Bug Report Sample

## BUG_001 - Login button allows submission with empty required fields

**Module:** User Login  
**Severity:** Medium  
**Priority:** High  
**Environment:** Web application - Chrome browser - Windows 10  
**Reported By:** Shathvika Kamalanathan  
**Status:** Open  

**Description:**  
The login form allows the user to click the Login button without entering a username or password. The system does not display clear validation messages for the required fields.

**Preconditions:**  
- User is on the login page

**Steps to Reproduce:**  
1. Navigate to the login page  
2. Leave the username field blank  
3. Leave the password field blank  
4. Click the Login button  

**Expected Result:**  
Validation messages should be displayed for both required fields, and the user should not be allowed to proceed.

**Actual Result:**  
The login form is submitted without showing proper validation messages.

**Reproducibility:**  
Always  

**Notes:**  
This issue affects input validation and may confuse users during login.
