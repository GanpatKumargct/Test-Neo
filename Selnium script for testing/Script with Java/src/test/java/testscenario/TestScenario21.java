package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario21 {
    public static void executeTest21() {
        /*
         * Dummy test run for scenario 21
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_21");

        try {
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.cssSelector(".promo-code")).click();
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_797");
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_775");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("user_name")).sendKeys("test_data_345");
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_511");
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
        executeTest21();
    }
}
