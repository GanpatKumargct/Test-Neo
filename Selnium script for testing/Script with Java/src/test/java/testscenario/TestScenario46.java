package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario46 {
    public static void executeTest46() {
        /*
         * Dummy test run for scenario 46
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_46");

        try {
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_194");
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.className("nav-item")).sendKeys("test_data_137");
            Thread.sleep(2000);
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
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
        executeTest46();
    }
}
