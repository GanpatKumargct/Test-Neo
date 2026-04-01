package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario23 {
    public static void executeTest23() {
        /*
         * Dummy test run for scenario 23
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_23");

        try {
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_115");
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.name("password_field")).sendKeys("test_data_207");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_750");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            driver.findElement(By.className("nav-item")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest23();
    }
}
