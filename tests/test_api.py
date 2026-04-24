import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "https://auth.vvdntech.com/api/v1"

COMMON_HEADERS = {
    "Content-Type": "application/json"
}

# ==================== TEST FUNCTIONS ====================
def test_tc001_verify_api_creates_user_with_valid_token_and_valid_payload():
    """
    Test ID: TC001
    Name: Verify API creates user with valid token and valid payload
    Expected Behavior: The API should successfully create a new user and return a 201 status code with the user's data.
    """
    url = f"{BASE_URL}/api/v1/users"
    headers = {
        **COMMON_HEADERS,
        "Content-Type": "application/json",
        "Authorization": "eyJraWQiOiJhMDUyYmIzZi02YmY0LTRhMzQtYjMwYi01OWQ5OGU0Yzg0MjAiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImF1ZCI6InB1YmxpYy1jbGllbnQiLCJuYmYiOjE3NzcwMDMxMjQsInNjb3BlIjpbIm9wZW5pZCJdLCJpc3MiOiJodHRwczovL2F1dGgudnZkbnRlY2guY29tIiwiZXhwIjoxNzc3MDg5NTI0LCJpYXQiOjE3NzcwMDMxMjQsImp0aSI6ImE5NGUwMWJjLWEzZDItNDM2Yy04NTY2LWRhZTM4ZjA0NzMxNyIsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXX0.b4RVwHaH5ZI8rP5nqRU1AAWzPdv3Om__JzX1Pan8Vg8MtUYZd_3loGIA6lDahW6oBOzOIEAZtstaFN30qAb2SPkAVp-aIDvagKMYENsnBLKE3eINXyZUYsCchAMnx8ibrr-bKNEp6WOwLjrrbAOsCg6ezYor5z1nUid8FaZSwn2e9bUEAapHf-wSJ1NwD76XPJqWMtUABd50Ey-28sFdjkRqEr9_3XHtGz8GxSewReqoNuj2ExvOpTwZ-14qooXocD0ftOg_iFC5_2fB6oZLyQIAb8y5r6x1sU2w_JwRAurRgUANxwnuGQHqudeSkCl0Qo065x5Xr-zQzgSVwRVmqA' \"
    }
    payload = {
      "email": "afsg@gmail.com",
      "designation": "SSE",
      "phoneNumber": "+911232435465",
      "empName": "ADFFGDG",
      "username": "equsswew",
      "password": "es@W12343",
      "empNo": "1232354365"
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201
    expected_response = {
      "status": 201,
      "message": "User registered successfully",
      "data": {
        "empNo": "1232354365",
        "empName": "ADFFGDG",
        "username": "equsswew",
        "email": "afsg@gmail.com",
        "designation": "SSE",
        "phoneNumber": "+911232435465"
      }
    }
    assert response.json() == expected_response

# def test_tc002_verify_api_returns_401_for_an_invalid_token():
#     """
#     Test ID: TC002
#     Name: Verify API returns 401 for an invalid token
#     Expected Behavior: The API should reject the request with a 401 Unauthorized status code due to the invalid token.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer invalidtoken123"
#     }
#     payload = {
#       "email": "test@example.com",
#       "designation": "QA",
#       "phoneNumber": "+919876543210",
#       "empName": "Test User",
#       "username": "testuser_invalidtoken",
#       "password": "Password@123",
#       "empNo": "987654"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 401
#     expected_response = {
#       "message": "Token Invalid or expired"
#     }
#     assert response.json() == expected_response

# def test_tc003_verify_api_returns_401_for_an_expired_token():
#     """
#     Test ID: TC003
#     Name: Verify API returns 401 for an expired token
#     Expected Behavior: The API should reject the request with a 401 Unauthorized status code due to the expired token.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer expired_access_token_placeholder_456"
#     }
#     payload = {
#       "email": "test@example.com",
#       "designation": "QA",
#       "phoneNumber": "+919876543210",
#       "empName": "Test User",
#       "username": "testuser_expiredtoken",
#       "password": "Password@123",
#       "empNo": "987654"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 401
#     expected_response = {
#       "message": "Token Invalid or expired"
#     }
#     assert response.json() == expected_response

# def test_tc004_verify_api_returns_403_for_an_unauthorized_user():
#     """
#     Test ID: TC004
#     Name: Verify API returns 403 for an unauthorized user
#     Expected Behavior: The API should reject the request with a 403 Forbidden status code because the user lacks creation permissions.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer token_for_user_without_permission_789"
#     }
#     payload = {
#       "email": "test@example.com",
#       "designation": "QA",
#       "phoneNumber": "+919876543210",
#       "empName": "Test User",
#       "username": "testuser_unauthorized",
#       "password": "Password@123",
#       "empNo": "987654"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 403
#     expected_response = {
#       "status": 403,
#       "message": "Access Denied",
#       "error": "Access Denied",
#       "path": "/api/v1/users"
#     }
#     assert response.json() == expected_response

# def test_tc005_verify_api_returns_400_for_missing_a_mandatory_field():
#     """
#     Test ID: TC005
#     Name: Verify API returns 400 for missing a mandatory field (username)
#     Expected Behavior: The API should return a 400 Bad Request status with a validation error message for the missing username.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer valid_access_token_placeholder_123"
#     }
#     payload = {
#       "email": "missinguser@example.com",
#       "designation": "SSE",
#       "phoneNumber": "+911232435466",
#       "empName": "Missing User",
#       "password": "es@W12343",
#       "empNo": "1232354366"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 400
#     expected_response = {
#       "status": 400,
#       "message": "Validation error",
#       "details": [
#         {
#           "field": "username",
#           "issue": "must not be blank"
#         }
#       ]
#     }
#     assert response.json() == expected_response

# def test_tc006_verify_api_returns_409_for_a_duplicate_username():
#     """
#     Test ID: TC006
#     Name: Verify API returns 409 for a duplicate username
#     Expected Behavior: The API should return a 409 Conflict status code indicating the username already exists.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer valid_access_token_placeholder_123"
#     }
#     payload = {
#       "email": "another@example.com",
#       "designation": "SSE",
#       "phoneNumber": "+911232435467",
#       "empName": "Duplicate User",
#       "username": "Admin",
#       "password": "es@W12343",
#       "empNo": "1232354367"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 409
#     expected_response = {
#       "status": 409,
#       "message": "User already exists",
#       "error": "User already exists with the given username: Admin",
#       "path": "/api/v1/users"
#     }
#     assert response.json() == expected_response

# def test_tc007_verify_api_returns_400_for_an_invalid_email_format():
#     """
#     Test ID: TC007
#     Name: Verify API returns 400 for an invalid email format
#     Expected Behavior: The API should return a 400 Bad Request status with a validation error for the malformed email address.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer valid_access_token_placeholder_123"
#     }
#     payload = {
#       "email": "invalid-email-format",
#       "designation": "SSE",
#       "phoneNumber": "+911232435468",
#       "empName": "Invalid Email",
#       "username": "invalidemailuser",
#       "password": "es@W12343",
#       "empNo": "1232354368"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 400
#     expected_response = {
#       "status": 400,
#       "message": "Validation error",
#       "details": [
#         {
#           "field": "email",
#           "issue": "must be a well-formed email address"
#         }
#       ]
#     }
#     assert response.json() == expected_response

# def test_tc008_verify_api_returns_400_for_an_empty_request_body():
#     """
#     Test ID: TC008
#     Name: Verify API returns 400 for an empty request body
#     Expected Behavior: The API should return a 400 Bad Request status with a validation error message for the empty payload.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         **COMMON_HEADERS,
#         "Content-Type": "application/json",
#         "Authorization": "Bearer valid_access_token_placeholder_123"
#     }
#     payload = {}
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 400
#     expected_response = {
#       "status": 400,
#       "message": "Validation error"
#     }
#     # Partial match is okay if more details are returned, but exact match is better if possible.
#     assert response.json() == expected_response

# def test_tc009_verify_api_validation_for_a_phone_number_without_a_country_code():
#     """
#     Test ID: TC009
#     Name: Verify API validation for a phone number without a country code
#     Expected: API returns 400 with a validation error for the phone number format.
#     """
#     url = f"{BASE_URL}/api/v1/users"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer <eyJraWQiOiJhMDUyYmIzZi02YmY0LTRhMzQtYjMwYi01OWQ5OGU0Yzg0MjAiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImF1ZCI6InB1YmxpYy1jbGllbnQiLCJuYmYiOjE3NzcwMDMxMjQsInNjb3BlIjpbIm9wZW5pZCJdLCJpc3MiOiJodHRwczovL2F1dGgudnZkbnRlY2guY29tIiwiZXhwIjoxNzc3MDg5NTI0LCJpYXQiOjE3NzcwMDMxMjQsImp0aSI6ImE5NGUwMWJjLWEzZDItNDM2Yy04NTY2LWRhZTM4ZjA0NzMxNyIsImF1dGhvcml0aWVzIjpbIlJPTEVfQURNSU4iXX0.b4RVwHaH5ZI8rP5nqRU1AAWzPdv3Om__JzX1Pan8Vg8MtUYZd_3loGIA6lDahW6oBOzOIEAZtstaFN30qAb2SPkAVp-aIDvagKMYENsnBLKE3eINXyZUYsCchAMnx8ibrr-bKNEp6WOwLjrrbAOsCg6ezYor5z1nUid8FaZSwn2e9bUEAapHf-wSJ1NwD76XPJqWMtUABd50Ey-28sFdjkRqEr9_3XHtGz8GxSewReqoNuj2ExvOpTwZ-14qooXocD0ftOg_iFC5_2fB6oZLyQIAb8y5r6x1sU2w_JwRAurRgUANxwnuGQHqudeSkCl0Qo065x5Xr-zQzgSVwRVmqA' \>",
#         **COMMON_HEADERS
#     }
#     payload = {
#         "email": "nocountrycode@example.com",
#         "designation": "SSE",
#         "phoneNumber": "1232435465",
#         "empName": "No Country Code",
#         "username": "nocountrycode",
#         "password": "es@W12343",
#         "empNo": "1232354369"
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     assert response.status_code == 400
#     expected_response = {
#         "status": 400,
#         "message": "Validation error",
#         "details": [
#             {
#                 "field": "phoneNumber",
#                 "issue": "must be in a valid international format"
#             }
#         ]
#     }
#     assert response.json() == expected_response