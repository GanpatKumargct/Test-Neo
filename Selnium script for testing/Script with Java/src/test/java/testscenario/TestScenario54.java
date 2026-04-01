package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario54 {
    public static void executeTest54() {
        /*
         * Dummy test run for scenario 54
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_54");

        try {
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.id("user_name")).sendKeys("test_data_556");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest54();
    }
}
