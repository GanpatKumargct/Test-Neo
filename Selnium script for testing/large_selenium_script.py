from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def execute_200_selenium_steps():
    """
    A dummy script containing exactly 200 Selenium action test cases/steps.
    Useful for testing AST parsers or LLM script parsers.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    # Step 1
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)
    
    # Block 1
    driver.find_element(By.ID, "firstName").send_keys("Alice")
    driver.find_element(By.ID, "lastName").send_keys("Smith")
    driver.find_element(By.ID, "userEmail").send_keys("alice@example.com")
    driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    
    # Block 2
    driver.find_element(By.ID, "subject_1").click()
    driver.find_element(By.ID, "subject_1").send_keys("Math")
    driver.find_element(By.ID, "hobbies_1").click()
    driver.find_element(By.ID, "currentAddress").send_keys("123 Main St, Springfield")
    driver.find_element(By.ID, "submit_form").click()
    
    # Block 3
    driver.find_element(By.ID, "modal_close").click()
    driver.find_element(By.ID, "nav_menu").click()
    driver.find_element(By.ID, "nav_item_1").click()
    driver.find_element(By.XPATH, "//button[@class='btn-primary']").click()
    driver.find_element(By.ID, "alert_accept").click()

    # Block 4
    driver.find_element(By.ID, "search_box").send_keys("laptop")
    driver.find_element(By.ID, "search_btn").click()
    driver.find_element(By.ID, "filter_brand").click()
    driver.find_element(By.ID, "brand_apple").click()
    driver.find_element(By.ID, "apply_filters").click()

    # Block 5
    driver.find_element(By.ID, "item_1").click()
    driver.find_element(By.ID, "add_to_cart").click()
    driver.find_element(By.ID, "view_cart").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "continue_shopping").click()

    # Block 6
    driver.find_element(By.ID, "search_box").clear()
    driver.find_element(By.ID, "search_box").send_keys("headphones")
    driver.find_element(By.ID, "search_btn").click()
    driver.find_element(By.ID, "item_2").click()
    driver.find_element(By.ID, "add_to_cart").click()

    # Block 7
    driver.find_element(By.ID, "view_cart").click()
    driver.find_element(By.ID, "remove_item_1").click()
    driver.find_element(By.ID, "update_cart").click()
    driver.find_element(By.ID, "checkout_btn").click()
    driver.find_element(By.ID, "login_email").send_keys("user@test.com")

    # Block 8
    driver.find_element(By.ID, "login_password").send_keys("password123")
    driver.find_element(By.ID, "login_submit").click()
    driver.find_element(By.ID, "shipping_address").send_keys("456 Elm St")
    driver.find_element(By.ID, "shipping_city").send_keys("Metropolis")
    driver.find_element(By.ID, "shipping_zip").send_keys("98765")

    # Block 9
    driver.find_element(By.ID, "continue_to_payment").click()
    driver.find_element(By.ID, "cc_number").send_keys("4111222233334444")
    driver.find_element(By.ID, "cc_exp").send_keys("12/25")
    driver.find_element(By.ID, "cc_cvv").send_keys("123")
    driver.find_element(By.ID, "place_order").click()

    # Block 10
    driver.find_element(By.ID, "order_confirmation").click()
    driver.find_element(By.ID, "view_receipt").click()
    driver.find_element(By.ID, "print_receipt").click()
    driver.find_element(By.ID, "back_to_home").click()
    driver.find_element(By.ID, "profile_link").click()

    # Block 11
    driver.find_element(By.ID, "edit_profile").click()
    driver.find_element(By.ID, "profile_phone").clear()
    driver.find_element(By.ID, "profile_phone").send_keys("9876543210")
    driver.find_element(By.ID, "save_profile").click()
    driver.find_element(By.ID, "logout_btn").click()

    # Block 12
    driver.find_element(By.ID, "nav_about").click()
    driver.find_element(By.ID, "nav_contact").click()
    driver.find_element(By.ID, "contact_name").send_keys("Test User")
    driver.find_element(By.ID, "contact_email").send_keys("test@test.com")
    driver.find_element(By.ID, "contact_message").send_keys("Hello world")

    # Block 13
    driver.find_element(By.ID, "send_message").click()
    driver.find_element(By.ID, "nav_careers").click()
    driver.find_element(By.ID, "job_search").send_keys("QA")
    driver.find_element(By.ID, "job_search_btn").click()
    driver.find_element(By.ID, "apply_job_1").click()

    # Block 14
    driver.find_element(By.ID, "applicant_name").send_keys("QA Tester")
    driver.find_element(By.ID, "applicant_resume").send_keys("/path/to/resume.pdf")
    driver.find_element(By.ID, "submit_application").click()
    driver.find_element(By.ID, "nav_blog").click()
    driver.find_element(By.ID, "blog_search").send_keys("automation")

    # Block 15
    driver.find_element(By.ID, "blog_search_btn").click()
    driver.find_element(By.ID, "read_more_1").click()
    driver.find_element(By.ID, "comment_body").send_keys("Great post!")
    driver.find_element(By.ID, "submit_comment").click()
    driver.find_element(By.ID, "subscribe_email").send_keys("qa@test.com")

    # Block 16
    driver.find_element(By.ID, "subscribe_btn").click()
    driver.find_element(By.ID, "social_facebook").click()
    driver.find_element(By.ID, "social_twitter").click()
    driver.find_element(By.ID, "social_linkedin").click()
    driver.find_element(By.ID, "footer_privacy").click()

    # Block 17
    driver.find_element(By.ID, "footer_terms").click()
    driver.find_element(By.ID, "go_to_top").click()
    driver.find_element(By.ID, "language_dropdown").click()
    driver.find_element(By.ID, "lang_es").click()
    driver.find_element(By.ID, "lang_en").click()

    # Block 18
    driver.find_element(By.ID, "theme_toggle").click()
    driver.find_element(By.ID, "theme_toggle").click()
    driver.find_element(By.ID, "feedback_btn").click()
    driver.find_element(By.ID, "feedback_text").send_keys("Looks good")
    driver.find_element(By.ID, "submit_feedback").click()
    
    # Block 19
    driver.find_element(By.ID, "dashboard_link").click()
    driver.find_element(By.ID, "widget_add").click()
    driver.find_element(By.ID, "widget_sales").click()
    driver.find_element(By.ID, "widget_save").click()
    driver.find_element(By.ID, "report_download").click()

    # Block 20
    driver.find_element(By.ID, "settings_link").click()
    driver.find_element(By.ID, "setting_notifications").click()
    driver.find_element(By.ID, "enable_email_notif").click()
    driver.find_element(By.ID, "enable_sms_notif").click()
    driver.find_element(By.ID, "save_settings").click()

    # Block 21
    driver.find_element(By.ID, "users_list").click()
    driver.find_element(By.ID, "add_user_btn").click()
    driver.find_element(By.ID, "new_user_name").send_keys("Bob")
    driver.find_element(By.ID, "new_user_role").send_keys("Admin")
    driver.find_element(By.ID, "save_new_user").click()

    # Block 22
    driver.find_element(By.ID, "edit_user_1").click()
    driver.find_element(By.ID, "user_status_active").click()
    driver.find_element(By.ID, "update_user").click()
    driver.find_element(By.ID, "delete_user_2").click()
    driver.find_element(By.ID, "confirm_delete").click()

    # Block 23
    driver.find_element(By.ID, "billing_link").click()
    driver.find_element(By.ID, "add_card_btn").click()
    driver.find_element(By.ID, "card_name").send_keys("Company Corp")
    driver.find_element(By.ID, "card_number").send_keys("5555666677778888")
    driver.find_element(By.ID, "save_card").click()

    # Block 24
    driver.find_element(By.ID, "upgrade_plan").click()
    driver.find_element(By.ID, "plan_pro").click()
    driver.find_element(By.ID, "confirm_upgrade").click()
    driver.find_element(By.ID, "view_invoices").click()
    driver.find_element(By.ID, "download_invoice_1").click()

    # Block 25
    driver.find_element(By.ID, "support_link").click()
    driver.find_element(By.ID, "new_ticket").click()
    driver.find_element(By.ID, "ticket_subject").send_keys("Need help")
    driver.find_element(By.ID, "ticket_desc").send_keys("System is slow")
    driver.find_element(By.ID, "submit_ticket").click()

    # Block 26
    driver.find_element(By.ID, "view_ticket_1").click()
    driver.find_element(By.ID, "reply_ticket").send_keys("Nevermind, fixed it")
    driver.find_element(By.ID, "send_reply").click()
    driver.find_element(By.ID, "close_ticket").click()
    driver.find_element(By.ID, "back_to_dashboard").click()

    # Block 27
    driver.find_element(By.ID, "api_keys").click()
    driver.find_element(By.ID, "generate_key").click()
    driver.find_element(By.ID, "key_name").send_keys("Prod Key")
    driver.find_element(By.ID, "create_key").click()
    driver.find_element(By.ID, "copy_key").click()

    # Block 28
    driver.find_element(By.ID, "revoke_key_1").click()
    driver.find_element(By.ID, "confirm_revoke").click()
    driver.find_element(By.ID, "webhooks").click()
    driver.find_element(By.ID, "add_webhook").click()
    driver.find_element(By.ID, "webhook_url").send_keys("https://hook.com")

    # Block 29
    driver.find_element(By.ID, "save_webhook").click()
    driver.find_element(By.ID, "test_webhook").click()
    driver.find_element(By.ID, "logs_link").click()
    driver.find_element(By.ID, "filter_errors").click()
    driver.find_element(By.ID, "refresh_logs").click()

    # Block 30
    driver.find_element(By.ID, "export_logs").click()
    driver.find_element(By.ID, "nav_analytics").click()
    driver.find_element(By.ID, "date_range").click()
    driver.find_element(By.ID, "range_7_days").click()
    driver.find_element(By.ID, "apply_date_range").click()

    # Block 31
    driver.find_element(By.ID, "chart_type_bar").click()
    driver.find_element(By.ID, "chart_type_line").click()
    driver.find_element(By.ID, "download_chart").click()
    driver.find_element(By.ID, "share_report").click()
    driver.find_element(By.ID, "share_email").send_keys("boss@test.com")

    # Block 32
    driver.find_element(By.ID, "send_share").click()
    driver.find_element(By.ID, "nav_marketing").click()
    driver.find_element(By.ID, "create_campaign").click()
    driver.find_element(By.ID, "campaign_name").send_keys("Summer Sale")
    driver.find_element(By.ID, "save_campaign").click()

    # Block 33
    driver.find_element(By.ID, "edit_email_template").click()
    driver.find_element(By.ID, "template_subject").send_keys("Big discounts")
    driver.find_element(By.ID, "save_template").click()
    driver.find_element(By.ID, "send_test_email").click()
    driver.find_element(By.ID, "launch_campaign").click()

    # Block 34
    driver.find_element(By.ID, "nav_inventory").click()
    driver.find_element(By.ID, "add_product").click()
    driver.find_element(By.ID, "product_name").send_keys("Shoes")
    driver.find_element(By.ID, "product_price").send_keys("50")
    driver.find_element(By.ID, "product_stock").send_keys("100")

    # Block 35
    driver.find_element(By.ID, "save_product").click()
    driver.find_element(By.ID, "edit_product_1").click()
    driver.find_element(By.ID, "product_price").clear()
    driver.find_element(By.ID, "product_price").send_keys("45")
    driver.find_element(By.ID, "update_product").click()

    # Block 36
    driver.find_element(By.ID, "delete_product_2").click()
    driver.find_element(By.ID, "confirm_del_product").click()
    driver.find_element(By.ID, "import_products").click()
    driver.find_element(By.ID, "upload_csv").send_keys("/files/products.csv")
    driver.find_element(By.ID, "start_import").click()

    # Block 37
    driver.find_element(By.ID, "nav_orders").click()
    driver.find_element(By.ID, "filter_pending").click()
    driver.find_element(By.ID, "view_order_123").click()
    driver.find_element(By.ID, "mark_shipped").click()
    driver.find_element(By.ID, "add_tracking_num").send_keys("TRK987654321")

    # Block 38
    driver.find_element(By.ID, "save_tracking").click()
    driver.find_element(By.ID, "print_shipping_label").click()
    driver.find_element(By.ID, "send_shipping_email").click()
    driver.find_element(By.ID, "back_to_orders").click()
    driver.find_element(By.ID, "filter_all").click()

    # Block 39
    driver.find_element(By.ID, "nav_reviews").click()
    driver.find_element(By.ID, "approve_review_1").click()
    driver.find_element(By.ID, "reject_review_2").click()
    driver.find_element(By.ID, "reply_review_3").click()
    driver.find_element(By.ID, "review_reply_text").send_keys("Thank you!")
    
    # Block 40
    driver.find_element(By.ID, "submit_review_reply").click()
    driver.find_element(By.ID, "logout_final").click()
    driver.find_element(By.ID, "login_again").click()
    driver.find_element(By.ID, "forgot_password").click()
    driver.find_element(By.ID, "reset_email").send_keys("user@test.com")

    # Final cleanup step
    driver.find_element(By.ID, "send_reset_link").click()
    driver.quit()

if __name__ == "__main__":
    execute_200_selenium_steps()
