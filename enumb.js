var colourRed = 1;
var colourGreen = 2;
var colourBlue = 3;
var Colour;
(function (Colour) {
    Colour[Colour["Red"] = 0] = "Red";
    Colour[Colour["Green"] = 1] = "Green";
    Colour[Colour["Blue"] = 2] = "Blue";
})(Colour || (Colour = {}));
;
// Also possible version - 
// enum Animals{Ant = 1, rat = 2, mouse = 3 };
var backgroundColour = Colour.Green;
