import inspect
import os
import jpype as jp
import atexit
import string

def normalize(text):
	# Import the required Java classes
	TurkishMorphology = jp.JClass('zemberek.morphology.TurkishMorphology')
	TurkishSentenceNormalizer = jp.JClass('zemberek.normalization.TurkishSentenceNormalizer')
	Paths = jp.JClass('java.nio.file.Paths')

	# Get the path to the (baseline) lookup files
	lookupRoot = Paths.get('zemberek/data/normalization')

	# Get the path to the compressed bi-gram language model
	lmPath = Paths.get('zemberek/data/lm/lm.2gram.slm')

	# Instantiate the morphology class with the default RootLexicon
	morphology = TurkishMorphology.createWithDefaults()

	# Initialize the TurkishSentenceNormalizer class
	normalizer = TurkishSentenceNormalizer(morphology, lookupRoot, lmPath)

	text = normalizer.normalize(text)
	text = text.translate(str.maketrans('', '', string.punctuation))
	while '  ' in text:
		text = text.replace('  ', ' ')
	return text
