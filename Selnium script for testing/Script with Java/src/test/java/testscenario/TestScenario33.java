package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario33 {
    public static void executeTest33() {
        /*
         * Dummy test run for scenario 33
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_33");

        try {
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            driver.findElement(By.className("nav-item")).sendKeys("test_data_357");
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_195");
            driver.findElement(By.id("user_name")).sendKeys("test_data_393");
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.className("nav-item")).sendKeys("test_data_502");
            driver.findElement(By.name("password_field")).sendKeys("test_data_707");
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_207");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest33();
    }
}
