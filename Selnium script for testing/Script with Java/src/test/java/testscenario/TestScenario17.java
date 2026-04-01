package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario17 {
    public static void executeTest17() {
        /*
         * Dummy test run for scenario 17
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_17");

        try {
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.id("user_name")).sendKeys("test_data_200");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_194");
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_406");
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_808");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.linkText("Log Out")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest17();
    }
}
