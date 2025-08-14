-- Adjust the absolute file path below to your local machine/server path.
-- Make sure 'LOCAL_INFILE=1' is enabled for your MySQL client/server when using LOCAL.
LOAD DATA LOCAL INFILE '/absolute/path/to/Customer-Churn-Records.csv'
INTO TABLE `customer_churn_raw`
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(`RowNumber`, `CustomerId`, `Surname`, `CreditScore`, `Geography`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary`, `Exited`, `Complain`, `Satisfaction_Score`, `Card_Type`, `Point_Earned`);