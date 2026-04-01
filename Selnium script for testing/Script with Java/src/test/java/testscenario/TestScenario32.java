package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario32 {
    public static void executeTest32() {
        /*
         * Dummy test run for scenario 32
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_32");

        try {
            Thread.sleep(2000);
            driver.findElement(By.name("password_field")).click();
            Thread.sleep(2000);
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.id("user_name")).sendKeys("test_data_546");
            Thread.sleep(2000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest32();
    }
}
