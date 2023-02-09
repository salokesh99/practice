class PointedClass {
    x: number ;
    y:number ;

// optional constructors need a question mark after the decalaration
// constructor(x?: number, y?:number){

    constructor(x: number, y:number){
        this.x = x;
        this.y = y;

    }
    draw() {
        console.log('drawing x and y', this.x, this.y)
    } ;

} ;


let pointObject =  new PointedClass(2, 4) ;


// we can change the value dynamically. 
pointObject.x = 11
pointObject.y = 12

pointObject.draw()
 