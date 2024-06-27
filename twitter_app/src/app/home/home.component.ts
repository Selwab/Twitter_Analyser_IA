import { Component, Injectable} from '@angular/core';
import { FormsModule, NgModel, ReactiveFormsModule, FormBuilder, FormControl, Validators}   from '@angular/forms';
import { Tweet } from '../interfaces/tweet';
import { CommonModule } from '@angular/common';
import { TweetComponent } from '../tweet/tweet.component';
import { TweetListComponent } from '../tweet-list/tweet-list.component';
import {MatIconModule} from '@angular/material/icon';
import {MatTabsModule} from '@angular/material/tabs';
import { MatNativeDateModule } from '@angular/material/core';
import {MatFormFieldModule, MatFormFieldControl} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';
import {environment} from '../../environment';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { isEmpty } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    FormsModule, 
    CommonModule, 
    TweetComponent, 
    TweetListComponent, 
    MatTabsModule, 
    MatIconModule,
    MatNativeDateModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatSelectModule,
    HttpClientModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  tweetsList: Tweet[] = [];
  filteredTweets: Tweet[] = [];
  tweetContent: string = '';
  selectedSentiment: number = 0;

  contentInput = new FormControl('', [
    Validators.required,
    this.validate_input.bind(this)
  ]);

  constructor(
    private http: HttpClient
  ){}

  ngOnInit() {
    this.get_all_tweets();
  }

  postTweet() {
    if(this.contentInput.invalid) {
      console.log("Error: ", this.contentInput.errors);
      return;
    }
    const payload = {
      text: this.contentInput.value,
      time: new Date(),
    }

    this.http.post(`${environment.apiUrl}/tweet`, payload).subscribe((saved_tweet:any) => {
      const newTweet: Tweet = {
        id: saved_tweet.id,
        text: saved_tweet.text,
        sentiment_id: saved_tweet.sentiment_id,
        image_url: saved_tweet.image_url,
        time: new Date(),
      }
  
      this.tweetsList.unshift(newTweet);
      this.contentInput.reset();
      console.log("Posted Tweets: ", saved_tweet);
    });
  }

  validate_input(control: FormControl): { [key: string]: any } | null {
    const input_value = control.value;
    if (!input_value || this.is_empty(input_value) || !this.count_words(input_value) || !this.contains_letters(input_value)) {
      return { 'validate_input': true };
    }
    return null;
  }

  is_empty(text: string): boolean {
    return text.trim().length === 0;
  }

  count_words(text: string): boolean {
    const min_words = 2;
    const words = text.trim().split(' ');
    const filter_blanc_words = words.filter(word => word !== '');
    return filter_blanc_words.length >= min_words;
  }

  contains_letters(text: string): boolean {
    const regex = /[a-zA-Z]/
    return regex.test(text)
  }
  
  get_all_tweets() {
    this.http.get<Tweet[]>(`${environment.apiUrl}/tweets`).subscribe((tweets) => {
      console.log("Id: ", tweets);
      tweets.sort((a, b) => new Date(b.time).getTime() - new Date(a.time).getTime());
      this.tweetsList = tweets;
      console.log("Fetched Tweets: ", this.tweetsList);
    });
  }

  filterTweets() {
    console.log("Selected Sentiment:", this.selectedSentiment);
    this.filteredTweets = [];
    for (const tweet of this.tweetsList) {
      if (tweet.sentiment_id == this.selectedSentiment) {
        this.filteredTweets.push(tweet);
      }
    }
    console.log("Filtered Tweets: ", this.filteredTweets);
  }
}
