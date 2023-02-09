export class PointedClass2 {
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

    // get X(){
    //     return this.x ;
    // }

    // set X(value) {
    //     if (value < 0 )
    //         throw new Error('Value can not be less than 0') ;
    //     this.x = value
    // }

} ;
