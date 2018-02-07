## Read in the data from daily_engagement.csv and project_submissions.csv 
## and store the results in the below variables.
## Then look at the first row of each table.

import unicodecsv
from datetime import datetime as dt

def read_csv(filename):
	with open(filename, 'rb') as f:
    	reader = unicodecsv.DictReader(f)
    	return list(reader)

def parse_date(date):
	if date = '':
		return None
	else:
		return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
	if i == '':
		return None
	else:
		return int(i)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions')

#Clean up the data types in the enrollments table
for enrollment in enrollments:
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
	enrollment['is_canceled'] = enrollment['is_canceled'] == True
	enrollment['is_udacity'] = enrollment['is_udacity'] == True
	enrollment['join_date'] = parse_date([enrollment['join_date']])

#Clean up the data types in the engagement table
for engagement_record in daily_engagement:
	engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
	engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
	engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
	engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
	engagement_record['utc_date'] = parse_date([engagement_record['utc_date']])

#Clean up the data types in the submissions table
for submission in project_submissions:
	submission['completion_date'] = parse_date(submission['completion_date'])
	submission['creation_date'] = parse_date(submission['creation_date'])