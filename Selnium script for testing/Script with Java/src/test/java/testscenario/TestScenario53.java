package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario53 {
    public static void executeTest53() {
        /*
         * Dummy test run for scenario 53
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_53");

        try {
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_917");
            driver.findElement(By.className("nav-item")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            driver.findElement(By.cssSelector(".promo-code")).click();
            Thread.sleep(2000);
            Thread.sleep(2000);
            driver.findElement(By.id("checkout_btn")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest53();
    }
}
