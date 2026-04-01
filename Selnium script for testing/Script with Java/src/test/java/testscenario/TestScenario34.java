package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario34 {
    public static void executeTest34() {
        /*
         * Dummy test run for scenario 34
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_34");

        try {
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_781");
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.name("password_field")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_404");
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_278");
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_803");
            driver.findElement(By.linkText("Log Out")).click();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest34();
    }
}
