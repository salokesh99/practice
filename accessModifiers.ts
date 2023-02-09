// 3 types of access modifiers in TS
// 1. Public
// 2. Private
// 3. protrected

class PointedClass1 {
    // private x: number ;
    // private y:number ;

// optional constructors need a question mark after the decalaration
constructor(private x?: number, private y?:number){}

    // constructor(x: number, y:number){
    //     this.x = x;
    //     this.y = y;

    // }
    public draw() {
        console.log('drawing x and y', this.x, this.y)
    } ;

    // getX(){
    //     return this.x
    // }

    // setX(value: number ) {
    //     if (value < 0 )
    //         throw new Error('Value can not be less than 0')
    //     this.x = value
    // }

    get X(){
        return this.x ;
    }

    set X(value) {
        if (value < 0 )
            throw new Error('Value can not be less than 0') ;
        this.x = value
    }

} ;


let pointObject1 =  new PointedClass1(2, 4) ;


// we can change the value dynamically. if it is public. Else we can not.
// pointObject1.x = 11
// pointObject1.y = 12

pointObject1.draw()
// let x = pointObject1.getX()
// pointObject1.setX(10)

let b =  pointObject1.X
pointObject1.X = 10