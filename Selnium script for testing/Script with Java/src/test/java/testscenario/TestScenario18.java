package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario18 {
    public static void executeTest18() {
        /*
         * Dummy test run for scenario 18
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_18");

        try {
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_599");
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            driver.findElement(By.linkText("Log Out")).click();
            Thread.sleep(2000);
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_402");
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest18();
    }
}
