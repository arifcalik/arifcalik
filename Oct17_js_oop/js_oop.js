class Rectangle{
    constructor(w, h, color){
        this.width = w;
        this.height = h;
        this.color = color;
    }
    calcArea(){
        return this.width * this.height;
    }
}

let rect = new Rectangle(4, 5, 'red');
console.assert(rect.width === 4);
console.assert(rect.height === 5);
console.assert(rect.color === "red");
console.assert(rect.calcArea() === 20);


class Person{
    constructor(firstName, lastName=null, age=null, mail=null){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = mail;
    }
    toString(){
        return this.firstName + " " + this.lastName + 
        " (age: " + this.age + ", email: " + this.email + ")"

    }
}

let person = new Person('Maria', 'Petterson', 22, 'mp@gmail.com');
console.assert(person.toString() == "Maria Petterson (age: 22, email: mp@gmail.com)");

function createPersonArray(){
    let persons = [person];
    let lexicon = new Person("Lexicon");
    persons.push(lexicon);
    let stefan = new Person("Stefan","Larsson",25);
    persons.push(stefan);
    let peter = new Person("Peter","Jansson",24,"ptr@live.com");
    persons.push(peter);
return persons;
}

let personlist = createPersonArray();
console.assert(personlist[0].firstName === 'Maria');
console.assert(personlist[0].lastName === 'Petterson');
console.assert(personlist[0].age === 22);
console.assert(personlist[0].email === 'mp@gmail.com');

console.assert(personlist[1].firstName === 'Lexicon');
console.assert(personlist[1].lastName === null);
console.assert(personlist[1].age === null);
console.assert(personlist[1].email === null);

console.assert(personlist[2].firstName === 'Stefan');
console.assert(personlist[2].lastName === 'Larsson');
console.assert(personlist[2].age === 25);
console.assert(personlist[2].email === null);

console.assert(personlist[3].firstName === 'Peter');
console.assert(personlist[3].lastName === 'Jansson');
console.assert(personlist[3].age === 24);
console.assert(personlist[3].email === 'ptr@live.com');

//console.log(personlist);

class Circle{
    constructor(r){
        this._radius = r;
    }
    set diameter(d){
        this._radius = d / 2;
    }
    get diameter(){
        return 2 * this._radius;
    }    
    get area(){
        return Math.PI * this._radius * this._radius;
    }        
}
let c = new Circle(2);
console.assert(c._radius === 2);
console.assert(c.diameter === 4);
console.assert(c.area === 12.566370614359172);
c.diameter = 1.6;
console.assert(c._radius === 0.8);
console.assert(c.diameter === 1.6);
console.assert(c.area === 2.0106192982974678);
class Point{
    constructor(x,y){
        this.x = x;
        this.y = y;
    }
    static distance(p1, p2){
        return Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 );
    }
}


let p1 = new Point(5, 5);
let p2 = new Point(9, 8);

console.assert( Point.distance(p1, p2) === 5);

