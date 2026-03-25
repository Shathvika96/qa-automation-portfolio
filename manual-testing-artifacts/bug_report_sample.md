# Bug Report

## BUG_001 - Login form submits without validating required fields

**Module:** User Login  
**Severity:** Medium  
**Priority:** High  
**Environment:** Web | Chrome (latest) | Windows 10  
**Reported By:** Shathvika Kamalanathan  
**Status:** Open  

---

## Description
The login form allows submission when both username and password fields are empty. No validation message is displayed to the user.

---

## Preconditions
- User is on the login page  

---

## Steps to Reproduce
1. Navigate to the login page  
2. Leave the username field empty  
3. Leave the password field empty  
4. Click the "Login" button  

---

## Expected Result
- Validation messages should be displayed for required fields  
- Form submission should be prevented  

---

## Actual Result
- Form is submitted without validation  
- No error message is displayed  

---

## Reproducibility
- Always  

---

## Impact
- Poor user experience due to missing validation  
- Invalid requests may be sent to backend systems  

---

## Notes
- Input validation should be enforced before form submission  
