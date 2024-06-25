import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterTweetsComponent } from './filter-tweets.component';

describe('FilterTweetsComponent', () => {
  let component: FilterTweetsComponent;
  let fixture: ComponentFixture<FilterTweetsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FilterTweetsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FilterTweetsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
