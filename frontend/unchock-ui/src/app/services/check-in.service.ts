import { Injectable } from '@angular/core';
import {CheckIn} from '../models/check-in.model';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CheckInService {

  constructor(private httpClient: HttpClient) { }

  getListOfCheckIns(): Observable<CheckIn[]> {
    return this.httpClient.get<CheckIn[]>(`http://localhost/api/check-ins/`);
  }

  createCheckIn(request: {booking_ref_num: string; passenger_last_name: string; passenger_first_name: string}): Observable<CheckIn[]> {
    return this.httpClient.post<CheckIn[]>(`http://localhost/api/check-ins/`, request);
  }
}
