package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario39 {
    public static void executeTest39() {
        /*
         * Dummy test run for scenario 39
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_39");

        try {
            driver.findElement(By.linkText("Log Out")).click();
            Thread.sleep(2000);
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_584");
            Thread.sleep(2000);
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest39();
    }
}
