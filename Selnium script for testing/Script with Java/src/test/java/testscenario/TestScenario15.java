package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario15 {
    public static void executeTest15() {
        /*
         * Dummy test run for scenario 15
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_15");

        try {
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("user_name")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.name("password_field")).sendKeys("test_data_682");
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest15();
    }
}
