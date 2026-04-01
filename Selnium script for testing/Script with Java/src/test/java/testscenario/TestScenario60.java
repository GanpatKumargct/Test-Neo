package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario60 {
    public static void executeTest60() {
        /*
         * Dummy test run for scenario 60
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_60");

        try {
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_169");
            driver.findElement(By.id("user_name")).sendKeys("test_data_601");
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).click();
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.className("nav-item")).sendKeys("test_data_793");
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).click();
            Thread.sleep(2000);
            driver.findElement(By.className("nav-item")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest60();
    }
}
