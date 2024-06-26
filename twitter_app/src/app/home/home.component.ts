import { Component, Inject, Injectable } from '@angular/core';
import { FormsModule, NgModel, ReactiveFormsModule}   from '@angular/forms';
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
  
  constructor(
    private http: HttpClient
  ){}

  tweetsList: Tweet[] = [];
  filteredTweets: Tweet[] = [];
  tweetContent: string = '';
  contentInput: string = '';
  selectedSentiment: number = 0;

  ngOnInit() {
    this.get_all_tweets();
  }

  postTweet() {
    const payload = {
      text: this.contentInput,
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
      this.tweetContent = this.contentInput;
      this.contentInput = '';
      console.log("Posted Tweets: ", saved_tweet);
    });
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
