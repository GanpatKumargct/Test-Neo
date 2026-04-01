package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario57 {
    public static void executeTest57() {
        /*
         * Dummy test run for scenario 57
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_57");

        try {
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.id("user_name")).sendKeys("test_data_920");
            Thread.sleep(2000);
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_705");
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.className("nav-item")).click();
            Thread.sleep(2000);
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_570");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest57();
    }
}
