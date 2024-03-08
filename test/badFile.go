package main

import "fmt"


var globalVar int = 10

type myStruct struct { 
    field1 int 
}

func main(){
    fmt.Println("Hello, World!") 

    
    var MyVariable int=5
    fmt.Println(MyVariable)

    result:=addNumbers(3, 4) 
    fmt.Println("Result:",result)
}

func addNumbers(a int,b int) int {
    return a+b 
}