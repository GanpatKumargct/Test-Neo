package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario2 {
    public static void executeTest2() {
        /*
         * Dummy test run for scenario 2
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_2");

        try {
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_418");
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_365");
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
        executeTest2();
    }
}
