package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario11 {
    public static void executeTest11() {
        /*
         * Dummy test run for scenario 11
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_11");

        try {
            driver.findElement(By.id("user_name")).sendKeys("test_data_488");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            Thread.sleep(2000);
            Thread.sleep(2000);
            driver.findElement(By.name("password_field")).click();
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.name("password_field")).sendKeys("test_data_961");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.cssSelector(".promo-code")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest11();
    }
}
