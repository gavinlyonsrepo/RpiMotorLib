

Software matrix
---------------------------------

Software matrix showing which classes are used to drive which components.

| Controller/Motor | DC motor    | Stepper Nema bipolar | Stepper 28BYJ Unipolar 5 |
| --------------- | ----------- | -------------------- | ------------------------ |
| transistor       | TranDc      | n/a                  | n/a                      |
| l298             | L298NMDc    | BYJMotor             | n/a                      |
| ULN2003          | n/a         | n/a                  | BYJMotor                 |
| a4988            | n/a         | A4988Nema            | n/a                      |
| a3967            | n/a         | A3967EasyNema        | n/a                      |
| Drv8825          | n/a         | A4988Nema            | n/a                      |
| L9110S           | DRV8833     | BYJMotor? WIP        | n/a                      |
| Drv8833          | DRV8833     | BYJMotor? WIP        | n/a                      |
| TB6612FNG        | TB6612FNGDc | BYJMotor             | n/a                      |
| LV8729           | n/a         | A4988Nema            | n/a                      |
