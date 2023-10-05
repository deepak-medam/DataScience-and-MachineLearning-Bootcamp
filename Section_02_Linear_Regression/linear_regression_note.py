"""
* Regression is the work horse of data science, business analytics an research.
* Regression is used whenever you want to model a phenomenon or make a prediction or discover the hidden relationships among things.

* Data Scientist would carefully formulate the question that they're looking to answer. A clear and well formulated question will
  dertermine the research and it will also affect the kind of data that you will go out and gather.
* Real world data is always missing. We have to always explore the data and visualize it so that we understand what it is that 
  we're looking at.

--- Process ---
* Formulate Question -> Gather Data -> Clearn Data -> Explore ad visualise Data -> Train Algorithm-> Evaluate
"""
"""
The first step is formulating the Question.
Question: How much revenue will our Movie make.?
What does movie revenue depend on?
To make this question much better the question could be
Can we use movie budgets to predict movie revenue? ( This is a much better question because it's testable which we can measure using data
and linear regression)

As Data Scientists we can look at this question and identify exactly what it is that we are trying to predict namely the movie revenue.
A Data Scientist would call this a dependent variable and in ML this would be called the target.
We can identify what it that we are using to make the prediction namely the movie budget A Data Scientist would call the budget the 
Independent varriable. In ML this would be called the feature.

We now have our Question, next step is to gather the data.
* We need data on our feature namely the movie budgets in £
* Second Data on target namely the movie revenue in £
* We get our data from https://www.the-numbers.com/
We now Clean the data
* In cleaning data step
    * We looked for missing data, Incomplete data, Inaccurate data
    * We done tiding by cheking the formatting of our data in detail.
In the next step we explore and visualize the data.

Why visualize our data, graphs and charts are incredibly useful to understand what it is that we are actually dealing with
because there is actually only so much you can learn by looking at a table of numbers, when you can look at chart you can spot problems
you can spot outliers, you can sport trends and you can sport patterns.
Pictures are incredibly informative.
From the graph we can see there is a trend upwards, highest budget films do indeed appear to have higher revenue but how much higher
exactly? How strong is the relationship. To answer this we need to turn to linear regression
Linear regression help us quantify this relationship

Theroy behind Regression
Linear regresion will get two kinds of data. It will get our film production budgets and it will get our film revenues.
The budget will be our feature also called the independet variable and the revenue is what we are trying to estimate that will be our target.

What Linear regression will do is try and represent the relationship between the budget and revenue as a straight line.
But What kind of line.?
We can plot y as a function of x and that's a line
The generic equation for a line is y = mx + c where m is the slope and c is the constant.
What part of line tells you how strong the relationship is between x and y, in this case the slope is the key.
The slope tells us how much y will change for a given change in x. The larges the value of slope the steeper the line becomes.

If there is not relationship between x and y then we would have a straight line where m=0. The stronge the relationship the steepr the
slope.
There's a big difference between machine learning and pure mathematics; in machine learning, we don't actually know the ture relationship
and that's why we refer to the slope and the intercept as parameters and these parameeters have to be estimated for our 
linear regression.
we change some notation we replace c with theta0 and slope coefficient m will be written as theta1 and the change the order
hthetax = theta0 + theta1.x where h stands for hypothesis

But where the line utlimately comes from, How do we kno wwhich line to draw. Looking at data we just have data points theres no line
and as a matter of fact you can draw a whole bunch of different lines through the same set of data points, So which line is best.?
which line would you choose.? Which line has best possible theta0 and theta1?
Real data is messy and if we were to draw line there would always be a gap between the actual value and the line.
In oher words there would be the difference between the actual data point and the point on the line.

* The point on the line is called the fitted value or the predicted value. It's these gaps that will helps us choose the best possible
intercept and the best possible slope for our line.
* The lines we draw from in the gaps are called residuals.
Q. Why will residuals help us choose the best possible line for our data?
The residuals can tell us how good the line is that we are drawing, now we have the measure all we have to do is look at the size of the
residuals and choose the line with the smalles residuals. Now our algorithm has a very clear objective.

The goal of our linear regression is going to be to calculate the line that minimizes these residuals.
But how should that work.?
The firs residual is gonna be the difference between the actual value y1 and the predicted value hthetax1, the second residual would also
be the differnce between the actual value and the fitted value and same is true for all the data points.

* If we calculate all the residual values these values will have 10, -6, 4, .. In this case we just cant add them up and fine the
lowest sum because some data points are below the line which will be negatives what we have to do instead is we have to turn all of
these numbers positive and the way we can do that is by squaring the residuals.
* Now we got the sum of squred residuals, a single number. This is the number the linear regression will try to minimize in order to
choose the best parameters for the line.
In other words to find the best possible fit for our regression, we need to choose our theta0 and theta1 that minmizes the sum of the 
squared residuals.
* This number is also referred to as residual sum of squares or RSS.

Analyze and result.
Once we fit our model the question we need to ask ourselves is are these parameters actually plausable
* For each pound we spend we should get 3.1pound in return. The intercept is at -7.2 million. How do we interpret that.?
What this intercept is literllay telling us is that a movie with a budget of zero would actually lose over 7million. That's a bit problematic
and unrealistic.

What should we conclude about our model.? We have to accept that our model is a dramatic simplification of the real world as such we 
should be a little bit careful on how much we believe the predictions of our model, especially at the extreme ends. Our model seems to
fit the data a lot worse at the extreme.
How much of the real world data is explained by our model.? For that we need some kind of measure or statistic and the measue we are going
to look at is called R squared also called the goodness of fit.
regression.score()

How would our model do if we added more features, like how long it took to make or if it's a sequel? Would we ger more realism? Would it
make our model perform better and make our predictions more accurate? And perhaps we should evaluate our model not just on the data tha we
used for training it, but on new data. What if the relationship tha we have here is actually non-linear.
What if somehow need to transform the data to get a better fit?
"""