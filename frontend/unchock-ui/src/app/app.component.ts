import {Component} from '@angular/core';
import {CheckIn} from './models/check-in.model';
import {FormControl, FormGroup} from '@angular/forms';
import {CheckInService} from './services/check-in.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'Unchock';

  errorSubmitting = false;
  submittingForm = false;
  checkIns: CheckIn[] = [];
  checkInForm = new FormGroup({
    passengerFirstName: new FormControl(),
    passengerLastName: new FormControl(),
    confirmationNumber: new FormControl()
  });

  constructor(private checkInService: CheckInService)  {
    this.checkInService.getListOfCheckIns().subscribe(checkIns => {
      this.checkIns = checkIns;
    });
  }

  flipError(): void {
    this.errorSubmitting = !this.errorSubmitting;
  }
  onSubmit(): void {
    this.submittingForm = true;
    this.checkInService.createCheckIn({
      passenger_first_name: this.checkInForm.get('passengerFirstName').value,
      passenger_last_name: this.checkInForm.get('passengerLastName').value,
      booking_ref_num: this.checkInForm.get('confirmationNumber').value
    }).subscribe(checkIns => {
      this.checkIns.push(...checkIns);
      this.checkInForm.reset();
      this.submittingForm = false;
    }, error => {
        this.flipError();
    });
  }
}
