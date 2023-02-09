class Pointed {
    x: number ;
    y:number ;

    draw() {
        console.log('drawing x and y', this.x, this.y)
    } ;

    drawDistance(another: Pointed) {
        // ..

    } ;
} ;


let point =  new Pointed() ;
point.x = 2;
point.y = 4;

point.draw()
 