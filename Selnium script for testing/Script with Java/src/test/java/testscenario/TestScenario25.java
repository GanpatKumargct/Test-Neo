package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario25 {
    public static void executeTest25() {
        /*
         * Dummy test run for scenario 25
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_25");

        try {
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.name("password_field")).sendKeys("test_data_555");
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            Thread.sleep(2000);
            driver.findElement(By.className("nav-item")).sendKeys("test_data_693");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_429");
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_896");
            driver.findElement(By.id("user_name")).sendKeys("test_data_534");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest25();
    }
}
