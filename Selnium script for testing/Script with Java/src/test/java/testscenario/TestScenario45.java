package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario45 {
    public static void executeTest45() {
        /*
         * Dummy test run for scenario 45
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_45");

        try {
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_473");
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).click();
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.linkText("Log Out")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest45();
    }
}
