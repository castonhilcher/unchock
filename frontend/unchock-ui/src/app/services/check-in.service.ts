import { Injectable } from '@angular/core';
import {CheckIn} from '../models/check-in.model';
import {HttpClient} from '@angular/common/http';
import {Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CheckInService {

  private checkInsSubject = new Subject<CheckIn[]>();
  private checkIns: CheckIn[] = [];
  constructor(private httpClient: HttpClient) { }

  getListOfCheckIns(): void {
    this.httpClient.get<CheckIn[]>(`http://localhost/api/check-ins/`).subscribe(checkIns => {
      this.checkIns.push(...checkIns);
      this.checkInsSubject.next(checkIns.slice());
    });
  }

  getCheckInSubject(): Observable<CheckIn[]> {
    return this.checkInsSubject.asObservable();
  }

  createCheckIn(request: {booking_ref_num: string; passenger_last_name: string; passenger_first_name: string}): void {
    this.httpClient.post<CheckIn[]>(`http://localhost/api/check-ins/`, request).subscribe(checkIns => {
      this.checkIns.push(...checkIns);

      this.checkInsSubject.next(checkIns.slice());
    });
  }
}
