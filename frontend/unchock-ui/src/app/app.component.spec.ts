import { TestBed, async } from '@angular/core/testing';
import { AppComponent } from './app.component';
import {CheckInService} from './services/check-in.service';
import {HttpClientModule} from '@angular/common/http';
import { By } from '@angular/platform-browser';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        AppComponent
      ],
      imports: [HttpClientModule],
      providers: [CheckInService]
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'Unchock'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('Unchock');
  });

  it('should have a h1 with value \'Unchock\'', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const element = fixture.debugElement.query(By.css('h1')).nativeElement;
    expect(element).toBeTruthy();
    expect(element.innerHTML).toBe('Unchock');
  });

  it('should have a h1 with value \'Unchock\'', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const element = fixture.debugElement.query(By.css('h1')).nativeElement;
    expect(element).toBeTruthy();
    expect(element.innerHTML).toBe('Unchock');
  });

  it('should have an p with h4 class with value \'Enter your information and we will check you in\'', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const element = fixture.debugElement.query(By.css('p.h4')).nativeElement;
    expect(element).toBeTruthy();
    expect(element.innerHTML).toBe('Enter your information and we will check you in');
  });

  it('should have an form', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const element = fixture.debugElement.query(By.css('form')).nativeElement;
    expect(element).toBeTruthy();
  });
});
