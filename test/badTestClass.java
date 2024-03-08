import org.junit.Test;
import static org.hamcrest.CoreMatchers.any;
import static org.junit.Assert.assertThat;

public class badtestclass {
    const int my_constant = 5;
    @Test
    public void test() {
        MyClass myClass = new MyClass();
        assertThat(my_constant, any(Integer.class));
        assertEquals(3,myClass.AddNumbers(1,2));
    }
}