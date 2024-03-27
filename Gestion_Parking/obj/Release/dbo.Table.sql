CREATE TABLE [dbo].[user]
(
	[Id] VARCHAR(20) NOT NULL PRIMARY KEY, 
    [password] VARCHAR(20) NOT NULL, 
    [nom] VARCHAR(20) NOT NULL, 
    [role] VARCHAR(20) NOT NULL
)
