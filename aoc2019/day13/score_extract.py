

def part2():
    with open('input.txt') as f:
        inp = f.read()

    data = [int(s) for s in inp.split(',')]

    print(data)
    print(sum(data[-252:]))


if __name__ == '__main__':
    part2()


"""
[37. 79. 96. 64.  8. 11. 52. 94. 65. 83. 14. 30. 31. 24. 50. 69. 85. 42.
 41. 52. 29. 11. 37. 69.  4. 66. 49.  3. 63. 40. 16. 81. 16. 34. 10. 59.
 24. 54. 62. 10. 76. 91. 42. 89. 97. 86. 85. 38. 60. 52. 19. 59. 90. 56.
 33. 49. 16. 76.  1. 78. 51. 47. 98. 45. 71.  5. 38. 22. 86. 40. 20. 66.
 56. 56. 34. 50. 45. 97.  1. 35. 75. 96. 82. 21. 93. 17. 86.  3. 66. 66.
 59. 27. 96. 96. 77. 56. 53. 24. 60. 70. 66. 42. 51. 13. 96. 58. 81. 87.
 22. 75.  3. 23. 53. 97. 59.  6.  5. 33. 48. 28. 16. 24. 82. 64. 74. 39.
  5. 15. 66. 97. 38.  4. 24. 84. 62. 47. 85. 14. 87. 11. 27. 75. 60. 62.
 62.  5. 42. 32. 24. 96. 30. 96. 60.  5. 88. 40. 35. 56.  1. 13. 14. 67.
 43. 58.  5. 49. 55.  4. 36. 38. 57. 74. 34. 90. 49. 21. 13. 21. 66. 85.
 17. 75.  8. 45. 73. 87.  2. 76. 54. 83. 76. 38. 74. 45. 97. 40. 62. 89.
 88. 49. 58. 75. 82. 95. 70.  6. 49. 68.  8. 86. 68. 57. 31.  9. 34. 39.
 89. 73. 68.  7. 62. 78. 37. 73. 67. 58.]
"""