import {inject, TestBed, getTestBed} from '@angular/core/testing';

import { CheckInService } from './check-in.service';
import {HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import {CheckIn} from '../models/check-in.model';


describe('CheckInService', () => {

  let injector: TestBed;
  let checkInService: CheckInService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule
      ], providers: [CheckInService]
    });

    injector = getTestBed();
    checkInService = injector.inject(CheckInService);
    httpMock = injector.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(checkInService).toBeTruthy();
  });

  it('should return an Observable<CheckIn[]> when calling get', () => {
    const checkIns = [new CheckIn(), new CheckIn()];

    checkInService.getListOfCheckIns().subscribe((checkInsResponse) => {
      expect(checkInsResponse).toEqual(checkIns);
      expect(checkInsResponse.length).toBe(2);
    });

    const req = httpMock.expectOne(`http://localhost/api/check-ins/`);
    expect(req.request.method).toBe('GET');
    req.flush(checkIns);

    httpMock.verify();
  });

  it('should return an Observable<CheckIn[]> when calling post', () => {
    const checkIn1 = new CheckIn();
    checkIn1.passenger_first_name = 'pfn';
    checkIn1.passenger_last_name = 'pln';
    checkIn1.booking_ref_num = 'brn';

    const checkIn2 = new CheckIn();
    checkIn2.passenger_first_name = 'pfn';
    checkIn2.passenger_last_name = 'pln';
    checkIn2.booking_ref_num = 'brn';

    const checkIns = [checkIn1, checkIn2];

    checkInService.createCheckIn({booking_ref_num: 'brn', passenger_first_name: 'pfn', passenger_last_name: 'pln'}).subscribe((checkInsResponse) => {
      expect(checkInsResponse).toEqual(checkIns);
      expect(checkInsResponse.length).toBe(2);
    });

    const req = httpMock.expectOne(`http://localhost/api/check-ins/`);
    expect(req.request.method).toBe('POST');
    req.flush(checkIns);

    httpMock.verify();
  });
});
