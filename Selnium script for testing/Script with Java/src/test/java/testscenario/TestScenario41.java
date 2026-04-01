package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario41 {
    public static void executeTest41() {
        /*
         * Dummy test run for scenario 41
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_41");

        try {
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.className("nav-item")).click();
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_358");
            driver.findElement(By.xpath("//button[@type='submit']")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest41();
    }
}
