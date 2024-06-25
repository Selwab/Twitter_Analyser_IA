import { Component } from '@angular/core';
import { FormsModule, NgModel, ReactiveFormsModule}   from '@angular/forms';
import { Tweet } from '../interfaces/tweet';
import { CommonModule } from '@angular/common';
import { TweetComponent } from '../tweet/tweet.component';
import { TweetListComponent } from '../tweet-list/tweet-list.component';
import {MatIconModule} from '@angular/material/icon';
import {MatTabsModule} from '@angular/material/tabs';
import { MatNativeDateModule } from '@angular/material/core';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';

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
    MatSelectModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  tweetsList: Tweet[] = [];
  filteredTweets: Tweet[] = [];
  tweetContent: string = '';
  contentInput: string = '';
  selectedSentiment: number = 0;

  private positiveImages = ['assets/sentiments/positive/1.jpeg', 'assets/sentiments/positive/2.jpg', 'assets/sentiments/positive/3.jpg'];
  private neutralImages = ['assets/sentiments/neutral/1.jpeg', 'assets/sentiments/neutral/2.png'];
  private negativeImages = ['assets/sentiments/negative/1.jpg', 'assets/sentiments/negative/2.jpg', 'assets/sentiments/negative/3.jpg', 'assets/images/negative/4.jpg'];

  postTweet() {
    const sentimentID = Math.floor(Math.random() * 3); // 0: Positive, 1: Neutral, 2: Negative
    const imageURL = this.getRandomImage(sentimentID);

    const newTweet: Tweet = {
      code: 1,
      content: this.contentInput,
      sentimentID: 0,
      imageURL: imageURL,
      hour: new Date(),
      date: new Date()
    }

    this.tweetsList.push(newTweet);
    this.tweetContent = this.contentInput;
    this.contentInput = '';
    console.log("Posted Tweets: ", newTweet);
  }

  filterTweets() {
    console.log("Selected Sentiment:", this.selectedSentiment);
    this.filteredTweets = [];
    for (const tweet of this.tweetsList) {
      if (tweet.sentimentID == this.selectedSentiment) {
        this.filteredTweets.push(tweet);
      }
    }
    console.log("Filtered Tweets: ", this.filteredTweets);
  }

  getRandomImage(sentimentID: number): string {
    switch (sentimentID) {
      case 0:
        return this.positiveImages[Math.floor(Math.random() * this.positiveImages.length)];
      case 1:
        return this.neutralImages[Math.floor(Math.random() * this.neutralImages.length)];
      case 2:
        return this.negativeImages[Math.floor(Math.random() * this.negativeImages.length)];
      default:
        return '';
    }
  }
}
